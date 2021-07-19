import re

import maya.cmds as mc

def maya_sel():
    sel = mc.ls(selection=True)
    return sel

def check(selection):
    """

    Args:
        selection (list(str)):

    """
    _asset = (r"^(?P<_asset>[A-Z]+)")
    _side = (r"(?P<_side>C|L|R)")
    _object = (r"(?P<_object>[A-Za-z0-9]+)")
    _type = (r"(?P<_type>jnt|jntEnd|geo|ctrl|loc|clstr|crv|nbs|ikhl|grp|parentConstraint|poleVectorConstraint)$")

    obj_name = re.compile(r"^(?P<_asset>\w+)_(?P<_loc>\w+)_(?P<_object>\w+)_(?P<_type>\w+)$")
    grp_name = re.compile(r"^(?P<asset>[A-Z]+)_(?P<object>SKL|CTRL|XTRAS|GEO)_(?P<type>grp)$")

    items_not_good = list()

    for item in selection:
        item_is_correct = obj_name.match(item)
        item_grp_is_correct = grp_name.match(item)

        if not item_is_correct and not item_grp_is_correct:
            items_not_good.append(item)

    return items_not_good


nomenclature_error = check(maya_sel())

if nomenclature_error:
    print("theses were not good:", nomenclature_error)
else:
    print("it's all good")
