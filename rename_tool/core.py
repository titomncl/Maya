import maya.cmds as mc
import os


def side_from_pos(obj):
    pos = mc.xform(obj, q=True, rp=True)

    if pos[0] < 0:
        side = "R"
    elif pos[0] > 0:
        side = "L"
    else:
        side = "C"

    return side


def ext_from_type(obj):
    ext = ""

    if mc.listRelatives(obj, type="mesh"):
        ext = "geo"
    if not mc.listRelatives(obj, type="shape"):
        ext = "grp"
    if mc.listRelatives(obj, type="nurbsCurve"):
        ext = "crv"

    return ext


def compute_new_name_obj(name, obj, num=None):

    item_name = os.environ["ITEM_NAME"]

    side = side_from_pos(obj)

    ext = ext_from_type(obj)

    if num:
        name += num

    new_name = item_name + "_" + side + "_" + name + "_" + ext

    return new_name


def rename(obj, new_name):
    mc.rename(obj, new_name)


def rename_multi_obj(base_name, selection):
    padding = len(str(len(selection) + 1)) + 1
    for num, obj in enumerate(selection):
        new_name = compute_new_name_obj(base_name, obj, str(num + 1).zfill(padding))
        rename(obj, new_name)
