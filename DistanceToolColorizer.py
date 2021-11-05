##DistanceToolColorVisibilty##
import maya.cmds as cmds

Width = 20
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
        cmds.setAttr(each+ '.overrideColor', height)