import maya.cmds as cmds
import re


def main():
    sel = cmds.ls(sl=True, l=True)

    for loc in sel:
        cmds.makeIdentity(loc, apply=True, t=True, r=True, s=True, n=False, pn=True)

        pos = cmds.xform(loc, q=True, rp=True)
        name = loc

        name = name.split("|")[-1]

        regex = re.compile(r"(?P<asset>[A-Z]+)_(?P<side>[CLR])_(?P<object>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)")

        name = regex.match(name)

        dict_name = name.groupdict()

        grp_name = dict_name["asset"] + "_SKL_grp"
        cmds.select(grp_name)

        joint_name = dict_name["asset"] + "_" + dict_name["side"] + "_" + dict_name["object"] + "_jnt"

        cmds.joint(p=pos, n=joint_name)
        cmds.joint(joint_name, e=True, zso=True)
