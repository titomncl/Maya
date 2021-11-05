import maya.cmds as mc

def test():
    print("hello! :)")

name = "cube"
mySel = mc.ls(sl=True)
assetName = "PROJECTNAME"
location = "C"
type = "geo"


for each in mySel:
    mc.rename(each, assetName + "_" + location + "_" + name + "_" + type)

