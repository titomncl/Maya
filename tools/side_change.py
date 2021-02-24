import re
import maya.cmds as mc

from CommonTools.concat import concat


def get_selection():
    return mc.ls(sl=True)


def side_change(side, selection):
    for object_name in selection:
        regex = re.compile(r"(?P<asset>[A-Z]+)_(?P<side>[CLR])_(?P<object>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)([0-9]+)?")

        name_ = object_name.split("|")[-1]

        name_is_correct = regex.match(name_)

        if name_is_correct:
            name = name_is_correct.groupdict()

            new_name = concat(name["asset"], side, name["object"], name["type"], separator="_")

            mc.rename(object_name, new_name)


def main(side):
    side_change(side, get_selection())
