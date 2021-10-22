##renameToolCore##
import maya.cmds as mc

asset_name = 'assetname'
location_name = 'location'
object_name = 'objectname'
## OBJECTIF FOR THIS TAKE SAME NAME OF 'EACH' OR MAKE A POSSIBILITY TO CHANGE OBJECT NAME, MAYBE WITH CHECK BOX ##
type_name = 'typename'
sl = True

for each in sel:
    mc.rename(each, asset_name + "_" + location_name + "_" + each + "_" + type_name)
#bonjour