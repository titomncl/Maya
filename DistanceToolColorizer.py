# DistanceToolColorVisibilty
import maya.cmds as cmds


def color_distance_tool():
    width = 20
    length = 4
    height = 18

    selection = cmds.ls(sl=True)
    for each in selection:
        cmds.setAttr(each + '.overrideEnabled', 1)

        if "width" in each:
            cmds.setAttr(each + '.overrideColor', width)

        elif "length" in each:
            cmds.setAttr(each + '.overrideColor', length)

        elif "height" in each:
            cmds.setAttr(each + '.overrideColor', height)


if __name__ == '__main__':
    import sys
    from copy import copy

    modules = copy(sys.modules)
    for module in modules:
        if "Maya" in module:
            sys.modules.pop(module)

    from Maya import common_ as cm

    cm.test()
