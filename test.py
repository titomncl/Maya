# create a locator by selecting deformable part of an object to place a joint after that
import maya.cmds as mc
import re

from CommonTools.concat import concat


def get_name():

    selection = mc.ls(sl=True)

    for object_name in selection:
        regex = re.compile(
            r"(?P<reference>.*:)?(?P<asset>[A-Z0-9_]+)_(?P<side>C|L|R)_(?P<object>[A-Za-z0-9]+)_(?P<type>[a-zA-Z+]+)(?P<selection>.*)?")

        name = regex.match(object_name)

        if name is None:
            mc.warning("Object " + object_name + " is not conform with the naming convention.")
        else:
            name = name.groupdict()

            create_loc_grp(name["asset"])

            locator_name = check_double(name)

            mc.select(selection)

            return locator_name


def create_locator(name):

    mc.cluster()

    sel = mc.ls(sl=True, long=True)

    for clstr in sel:
        pos = mc.xform(clstr, q=True, rp=True)
        mc.delete(clstr)
        my_loc = mc.spaceLocator(p=pos, n=name)
        mc.xform(my_loc, cp=1)

    mc.parent(name, "*locators_grp")

    mc.makeIdentity(a=True, t=True, r=True, s=True, n=False, pn=True)


def create_loc_grp(asset):
    mc.select(all=True, hi=True)

    xtras = False
    locator_bool = False

    xtras_n = asset + "_XTRAS_grp"
    locator_grp = asset + "_C_locators_grp"

    for element in mc.ls(sl=True):
        if "XTRAS" in element:
            xtras = True
        if "locators_grp" in element:
            locator_bool = True

    if not xtras:
        mc.group(p=asset + "_grp", n=xtras_n, em=True)
        mc.group(p=xtras_n, n=locator_grp, em=True)
    elif not locator_bool:
        mc.group(p=xtras_n, n=locator_grp, em=True)

    mc.select(clear=True)


def check_double(groupdict):
    mc.select(all=True, hi=True)

    name = groupdict["asset"] + "_" + groupdict["side"] + "_" + groupdict["object"]

    count = 0

    for element in mc.ls(sl=True):
        if "locator" in element and name in element and not "Shape" in element:
            print(element)
            count+=1
            mc.rename(element, name + str(count).zfill(2) + "_locator")

    if count == 0:
        name = name + "_locator"
    else:
        name = name + str(count + 1).zfill(2) + "_locator"
    return name


def locator():

    locator = get_name()

    if locator not in ["", None]:
        create_locator(locator)


# TRANSFORM LOC TO JNT
def loc_to_jnt():
    sel = mc.ls(sl=True, l=True)

    for loc in sel:
        pos = mc.xform(loc, q=True, rp=True)
        name = loc

        name = name.split("|")[-1]

        regex = re.compile(r"(?P<asset>[A-Z0-9_]+)_(?P<side>C|L|R)_(?P<object>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)")

        name = regex.match(name)

        dict_name = name.groupdict()

        grp_name = dict_name["asset"] + "_RIG_grp"
        mc.select(grp_name)

        joint_name = dict_name["asset"] + "_" + dict_name["side"] + "_" + dict_name["object"] + "_jnt"

        mc.joint(p=pos, n=joint_name)
        mc.joint(joint_name, e=True, zso=True)


def abs_grp():
    sel = mc.ls(sl=True)

    for obj in sel:
        ctrl_pattern = re.compile(r"^(?P<asset>[A-Z0-9_]+)_(?P<side>C|L|R)_(?P<object>[A-Za-z0-9]+)_(?P<type>ctrl|grp)")

        obj_is_conform = ctrl_pattern.match(obj)

        if obj_is_conform:
            obj_name = obj_is_conform.groupdict()

            grp_name = concat(obj_name["asset"], obj_name["side"], obj_name["object"], "Abs_grp", separator="_")

            mc.group(obj, w=True, n=grp_name)


def colorize_ctrl():
    ULTIMATE_COLOR = 14
    CENTER_COLOR = 17
    RIGHT_COLOR = 13
    LEFT_COLOR = 6

    selection = mc.ls('*ctrlShape')

    for ctrl in selection:
        mc.setAttr(ctrl + '.overrideEnabled', 1)
        print(ctrl)
        if '_C_' in ctrl:
            if "ultimate" in ctrl:
                mc.setAttr(ctrl + '.overrideColor', ULTIMATE_COLOR)
            else:
                mc.setAttr(ctrl + '.overrideColor', CENTER_COLOR)
        elif '_R_' in ctrl:
            mc.setAttr(ctrl + '.overrideColor', RIGHT_COLOR)
        elif '_L_' in ctrl:
            mc.setAttr(ctrl + '.overrideColor', LEFT_COLOR)


def correct_constraint():

    constraint_regex = re.compile(r"^(?P<asset>[A-Z]+)_(?P<side>[CLR])_(?P<object>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)_(?P<constraint>.+Constraint)([0-9])$")

    sel = mc.ls("*Constraint*")

    for element in sel:

        name_is_correct = constraint_regex.match(element)

        if name_is_correct:
            name = name_is_correct.groupdict()

            new_object_name = name["object"] + name["type"].capitalize()

            corrected_name = concat(name["asset"], name["side"], new_object_name, name["constraint"], separator="_")

            mc.rename(element, corrected_name)


if __name__ == '__main__':
    pass