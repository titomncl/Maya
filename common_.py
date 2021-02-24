import maya.cmds as mc

from qtpy.QtWidgets import QMainWindow
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

# import os
# import re

# from pattern import Type, PROJECT_PATTERN, SIDE_PATTERN, OBJECT_NAME_PATTERN
# from pattern import PROJECT_GRP, MAIN_GRP, OBJECT_PATTERN

# from Maya.pattern import Type
# from CommonTools.concat import concat


def test():
    print("Hello World!")


def get_main_window():

    maya_main_window = omui.MQtUtil.mainWindow()
    maya_main_window_instance = wrapInstance(int(maya_main_window), QMainWindow)

    return maya_main_window_instance

# def get_project():

    # print(Type.pattern(Type.get(Type.GRP)))

    # group_re = re.compile(PROJECT_GRP)
    #
    # groups = mc.ls("*_grp")
    #
    # if len(groups) > 0:
    #     for group in groups:
    #         is_asset = group_re.match(group)
    #
    #         print(PROJECT_GRP)
    #
    #         if is_asset:
    #             print(group)
    #             break
    # else:
    #     raise RuntimeWarning("No project found")