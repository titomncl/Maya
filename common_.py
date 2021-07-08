import maya.cmds as mc

import os

import subprocess

from PySide2.QtWidgets import QMainWindow
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

from Maya.globals import DEV_PATH


def test():
    print("Hello World!")


def update_popup():

    title = "Update"

    msg = "An update has been made. Please, restart Maya to apply the modifications."

    restart = "Restart"
    cancel = "Later"

    btn = [restart, cancel]

    choice_ = mc.confirmDialog(t=title, m=msg, b=btn, db=restart, cb=cancel, ds=cancel)

    if choice_ == restart:

        maya_pyc()

        subprocess.Popen('"C:\\Program Files\\Autodesk\\Maya2019\\bin\\maya.exe"', shell=True)
        mc.quit(force=True)


def maya_pyc():

    maya_path = DEV_PATH + "/Maya/"

    files_ = os.listdir(maya_path)

    pyc_files = [file_ for file_ in files_ if ".pyc" in file_]

    for pyc_file in pyc_files:
        os.remove(os.path.join(maya_path, pyc_file))


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
    clean_mode()

    mc.file(rename=filepath)
    mc.file(save=True, type="mayaAscii")


def open_file(filepath):

    mc.file(filepath, open=True, lrd="all", f=True)


def get_dag_objects(all_=True):
    """
    Get a list of object
    Args:
        all_ (bool): If true, get the visible dag objects. If false, get the current selection

    Returns:
        list(str):

    """
    if all_:
        return mc.ls(v=True)
    else:
        return mc.ls(sl=True)


def clean_mode():
    select_list_object()

    try:
        freeze_transforms()
    except TypeError as e:
        print("An error occurred with the freeze transforms:", e)

    delete_history()


def select_list_object():
    mc.select(get_dag_objects())


def delete_history():
    mc.delete(ch=True)


def freeze_transforms():
    mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)
