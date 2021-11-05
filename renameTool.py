import maya.cmds as mc
from Maya.tree.create_tree import ProjectTree

def test():
    print("hello! :)")

name = "cube"
mySel = mc.ls(sl=True)
assetName = ProjectTree().asset
location = "C"
type = "geo"


for each in mySel:
    mc.rename(each, assetName + "_" + location + "_" + name + "_" + type)

