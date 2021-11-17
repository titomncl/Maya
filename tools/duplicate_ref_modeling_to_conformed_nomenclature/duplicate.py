import maya.cmds as mc

mc.duplicate(mc.ls(sl=True))

selection_ref = mc.ls(sl=True)

print(selection_ref)
for obj_to_rename in selection_ref:
    if "Reference" in obj_to_rename:
        new_obj_name = obj_to_rename.replace("Reference", "")
        new_obj_name = new_obj_name.replace("geo1", "geo")
        mc.rename(obj_to_rename, new_obj_name)

mc.parent(w=True)

