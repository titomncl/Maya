#Check name
import re

def check(selected)
    _(R|C|L)_([A-Za-z0+9]+) (jnt|jntEnd|geo|ctrl|loc|clstr|crv|nbs|ikhl|grp|parentConstraint|poleVectorConstraint)
    _asset = (r"^([A-Z]+)")
    _loc = (r"([R|C|L])")
    _object = (r"([A-Za-z0-9]+)")
    _type = (r"(jnt|jntEnd|geo|ctrl|loc|clstr|crv|nbs|ikhl|grp|parentConstraint|poleVectorConstraint)$")

    objName = _asset, _loc, _object, _type
    grpName = (r"^([A-Z]+)_(SKL|CTRL|XTRAS|GEO)_(grp)")
    list_nomenclatureError = list()

    for each in selected:
        match = objName.match(each)
        matchGRP = grpName.match(each)

            if not match and not matchGRP in each:
                list_nomenclatureError.append(each)

            if list_nomenclatureError != []:
                raise RuntimeError ("/!\ Your nomenclature name is wrong, rename it please/!\ ", list_nomenclatureError)


