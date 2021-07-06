import os
import maya.cmds as mc

from CommonTools.concat import concat

from Maya.common_ import get_filepath


def info_from_filepath(filepath):
    _, filename = os.path.split(filepath)
    filename, _ = os.path.splitext(filename)

    project = filename.split("_")[0]
    department = filename.split("_")[1]

    return project, department


def create_mod_grp(prj, dpt):
    prj_grp = mc.group(n=concat(prj, "grp", separator="_"), em=True, w=True)

    dpt_grp = mc.group(n=concat(prj, dpt, "grp", separator="_"), em=True)

    mc.parent(dpt_grp, prj_grp)

    mc.select(dpt_grp, r=True)

    mc.createDisplayLayer(n=concat(prj, dpt, "layer", separator="_"), number=1)


def create_rig_grp(prj, dpt):
    prj_grp = mc.group(n=concat(prj, "grp", separator="_"), em=True, w=True)

    dpt_grp = mc.group(n=concat(prj, dpt, "grp", separator="_"), em=True)

    mc.parent(dpt_grp, prj_grp)

    mc.select(dpt_grp, r=True)

    mc.createDisplayLayer(n=concat(prj, dpt, "layer", separator="_"), number=1)


if __name__ == '__main__':

    all_obj = mc.ls(dag=True)

    groups_ = list()

    for obj in all_obj:
        if not "shape" in obj.lower():
            is_not_group = mc.listRelatives(obj, s=True)

            if not is_not_group:
                if "MOD"



    # try:
    #     filepath = get_filepath()
    # except RuntimeError as e:
    #     print(e)
    # else:
    #     if filepath:
    #         project, department = info_from_filepath(filepath)


