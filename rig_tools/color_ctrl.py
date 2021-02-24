import maya.cmds as cmds

ULTIMATE_COLOR = 14
CENTER_COLOR = 17
RIGHT_COLOR = 13
LEFT_COLOR = 6

def main():

    selection = cmds.ls('*ctrlShape')

    for ctrl in selection:
        cmds.setAttr(ctrl + '.overrideEnabled', 1)
        print(ctrl)
        if '_C_' in ctrl:
            if "ultimate" in ctrl:
                cmds.setAttr(ctrl + '.overrideColor', ULTIMATE_COLOR)
            else:
                cmds.setAttr(ctrl + '.overrideColor', CENTER_COLOR)
        elif '_R_' in ctrl:
            cmds.setAttr(ctrl + '.overrideColor', RIGHT_COLOR)
        elif '_L_' in ctrl:
            cmds.setAttr(ctrl + '.overrideColor', LEFT_COLOR)

