import maya.cmds as mc

import os

import subprocess

from PySide2.QtWidgets import QMainWindow
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

from CommonTools.concat import concat


def test():
    print("Hello World!")


def raise_error(e):
    mc.error(str(e))

def raise_warning(e):
    mc.warning(str(e))

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


def get_objects(dag=True):
    """
    Get a list of object
    Args:
        dag (bool): If true, get the visible dag objects. If false, get the current selection

    Returns:
        list(str):

    """
    if dag:
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
    mc.select(get_objects())


def delete_history():
    mc.delete(ch=True)


def freeze_transforms():
    mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=True)


def quick_renaming():
    from Maya.tree.create_tree import ProjectTree

    sel = get_objects(dag=False)

    asset_name = ProjectTree().asset

    for obj in sel:
        mc.rename(obj, concat(asset_name, "C", obj, "geo", separator="_"))


def import_ref_to_scene():
    refs = mc.ls(rf=True)

    for ref in refs:
        ref_file = mc.referenceQuery(ref, f=True)
        ref_namespace = mc.referenceQuery(ref, ns=True)
        mc.file(ref_file, ir=True)
        mc.namespace(mv=[ref_namespace, ":"], f=True)


def get_root_for_abc_export():
    sel = mc.ls(sl=True)

    root = ""

    for obj in sel:
        parent_obj = mc.listRelatives(obj, p=True)[-1]
        main_grp_obj = mc.listRelatives(parent_obj, p=True)

        if main_grp_obj and len(main_grp_obj) == 1:
            print(main_grp_obj[-1], parent_obj)

            root += "-root |{}|{} ".format(main_grp_obj[-1], parent_obj)

        else:
            # root += "-root |{}|{}".format(parent_obj, obj)
            raise RuntimeError("Only meshes are accepted for the moment")

    return root


def export_obj(filepath):
    mc.loadPlugin("objExport.mll")

    mc.file(filepath, f=True, op="groups=1;ptgroups=1;materials=1;smoothing=2;normals=1",
            typ="OBJexport", pr=True, es=True)


def export_alembic(command):
    mc.loadPlugin("AbcExport.mll")
    mc.AbcExport(j=command)
