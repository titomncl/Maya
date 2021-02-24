# Check naming nomenclature
import maya.cmds as mc
import re

from CommonTools.concat import concat

def check(selection):
    _asset = (r"^(?P<asset>[A-Z]+)")
    _side = (r"(?P<side>C|L|R)")
    _object = (r"(?P<object>[A-Za-z0-9]+)")
    _type = (r"(?P<type>jnt|jntEnd|geo|geoBase|ctrl|locator|clstr|crv|nbs|ikhl|grp|follicle|.+Constraint)$")

    obj_regex = re.compile(concat(_asset, _side, _object, _type, separator="_"))
    grp_regex = re.compile(r"^(?P<asset>[A-Z]+)_(?P<object>SKL|CTRL|XTRAS|GEO)_(?P<type>grp)$")

    list_error = list()

    for each in selection:
        match = obj_regex.match(each)
        grp_match = grp_regex.match(each)

        if not match and not grp_match and not "effector" in each:
            list_error.append(each)

    if list_error != []:
        raise RuntimeError("Some error in naming", list_error)
        # try:
        #     match = obj_regex.match(each)
        #     match = match.groupdict()
        #     checked = True
        # except:
        #     try:
        #         grp_match = grp_regex.match(each)
        #         grp_match = grp_match.groupdict()
        #         checked = True
        #     except:
        #         if "effector" not in each:
        #             list_error.append(each)


def maya_sel():
    sel = mc.ls(sl=True)

    return sel

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


def main():

    correct_constraint()

    try:
        check(maya_sel())
    except RuntimeError as e:
        print(e)
    # check_pass, lst_error = check(maya_sel())
    #
    # if check_pass and lst_error == []:
    #     print("No error !")
    # else:
    #     print("Some error in naming : ")
    #     for each in lst_error:
    #         print(each)
