#Check name

import re
import maya.cmds as mc

def check(selected):
    _asset = (r"^([A-Z]+)")
    _loc = (r"([R|C|L])")
    _object = (r"([A-Za-z0-9]+)")
    _type = (r"(jnt|jntEnd|geo|ctrl|loc|clstr|crv|nbs|ikhl|grp|parentConstraint|poleVectorConstraint)$")

    obj_name = re.compile(r"(?P<_asset>\w+) (?P<_loc>\w+) (?P<_object>\w+) (?P<_type>\w+)")
    grp_name = re.compile(r"^(?P<asset>[A-Z]+)_(?P<object>SKL|CTRL|XTRAS|GEO)_(?P<type>grp)$")
    list_nomenclature_error = list()

    for each in selected:
        match = obj_name.match(each)
        match_grp = grp_name.match(each)

        if not match and not match_grp in each:
                list_nomenclature_error.append(each)

        if list_nomenclature_error != []:
            raise RuntimeError ("/!\ Your nomenclature name is wrong, rename it please /!\ ", list_nomenclature_error)

def maya_sel():
    sel = mc.ls(sl=True)

    return sel
