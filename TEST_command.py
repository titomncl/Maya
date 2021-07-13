import re

def maya_sel():
    sel = mc.ls(sl=True)
    return sel

#def check(select):
_name = (r"^(?P<asset>[A-Z]+)")
_side = (r"(?P<side>C|L|R)")
_object = (r"(?P<object>[A-Za-z0-9]+)")
_type =  (r"(?P<type>jnt|jntEnd|geo|ctrl|loc|clstr|crv|nbs|ikhl|grp|parentConstraint|poleVectorConstraint)$")

object_naming = re.compile(concat(_asset, _side, _object, _type, separator="_"))

<for each in maya_sel():
    print(_name)

