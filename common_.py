import maya.cmds as mc

import os
import sys

import subprocess

from qtpy.QtWidgets import QMainWindow
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

from shutil import copyfile

from Maya.globals import USER_PATH

from Maya import init_env

from CommonTools.concat import concat


def test():
    print("Hello World!")

def update_user_setup():
    source_file = os.path.join(os.path.dirname(init_env.__file__), "init_env.py").replace("\\", "/")

    destination_file = concat(USER_PATH, "Documents/maya/2019/scripts/init_env.py", separator="/")

    updated = False

    if not os.path.isfile(destination_file):
        copyfile(source_file, destination_file)
        updated = True
    else:
        time_src = os.stat(source_file)
        time_dst = os.stat(destination_file)

        if time_src.st_mtime > time_dst.st_mtime:

            copyfile(source_file, destination_file)
            updated = True

    if updated:
        update_popup()

def update_shelf():
    source_file = os.path.join(os.path.dirname(init_env.__file__), "shelves/shelf_VSPA_TOOLS.mel").replace("\\", "/")
    destination_file = concat(USER_PATH, "/Documents/maya/2019/prefs/shelves/shelf_VSPA_TOOLS.mel")

    copyfile(source_file, destination_file)


def update_popup():

    title = "Update"

    msg = "An update has been made. Please, restart Maya to apply the modifications."

    restart = "Restart"
    cancel = "Later"

    btn = [restart, cancel]

    choice_ = mc.confirmDialog(t=title, m=msg, b=btn, db=restart, cb=cancel, ds=cancel)

    if choice_ == restart:
        subprocess.Popen('"C:\\Program Files\\Autodesk\\Maya2019\\bin\\maya.exe"', shell=True)
        mc.quit(force=True)


def get_main_window():

    maya_main_window = omui.MQtUtil.mainWindow()
    maya_main_window_instance = wrapInstance(int(maya_main_window), QMainWindow)

    return maya_main_window_instance


def get_filepath():
    """
    Query the filepath of the scene

    Returns:
        str: filepath

    """
    filepath = mc.file(q=True, sn=True)

    if filepath:
        return filepath
    else:
        raise RuntimeError("File not saved.")


def save_as(filepath):
    """
    Args:
        filepath (str): path/filename.ma

    """
    mc.file(rename=filepath)
    mc.file(save=True, type="mayaAscii")

def open_file(filepath):

    mc.file(filepath, open=True, lrd="all", f=True)
