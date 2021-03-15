def main():
    import os
    import sys
    import maya.cmds as cmds

    print("INIT_ENV")

    ############ HOT-FIX ############
    os.environ["PFE_PROJET"] = "G:/.shortcut-targets-by-id/1LKqbnGUt5-Lrfl9lElekEI0vY2DOIoog/VSPA"
    ROOT_PATH = "G:/.shortcut-targets-by-id/1LKqbnGUt5-Lrfl9lElekEI0vY2DOIoog"

    project_name = ipm_package()

    ############# PFE ENV #############
    import os
    import sys

    PFE_ENV = ROOT_PATH + "/" + project_name

    DEV_ENV = "E:/DEV"

    if os.path.isdir(DEV_ENV):
        venv = DEV_ENV + "/venv/Lib/site-packages"
    else:
        DEV_ENV = PFE_ENV + "/DEV/main"
        venv = DEV_ENV + "/venv/Lib/site-packages"

    sys.path.append(PFE_ENV)
    sys.path.append(DEV_ENV)
    sys.path.append(venv)

    os.environ["PFE_ENV"] = PFE_ENV
    os.environ["DEV_ENV"] = DEV_ENV

    ############ HOT-FIX ############
    os.environ["PFE_PROJET"] = PFE_ENV

    ########### PFE ENV END ###########

    ########## AUTO UDPATE ##########
    from Maya import common_

    cmds.evalDeferred(common_.update_user_setup)


def ipm_package():
    import sys
    import os

    ############ USER PROFILE ############
    USER_PATH = os.environ['USERPROFILE'].replace('\\', '/')
    print(USER_PATH.upper())

    ############ ADD IPM IN PYTHONPATH ############
    sys.path.append(USER_PATH + "/ISART_PROJECT_MANAGER/")
    sys.path.append(USER_PATH + '/ISART_PROJECT_MANAGER/PY/')

    import ipm
    import Vinci

    ### VARIABLES GENERALES ###
    project_name = ipm.ctFindProject()

    if project_name:
        print('NOM_PROJET : %s' % project_name)
        props = ipm.ctFindAsset(project_name, 'CHARA\\*')
        print('LISTE_PERSOS : %s' % ' '.join(props))
        modules = ipm.ctFindAsset(project_name, 'SET\\*\\MODULES\\*')
        print('LISTE_MODULES : %s' % ' '.join(modules))

        ### MENU ISART ###
        import maya.cmds as cmds
        import maya.mel as mel

        cmds.evalDeferred(ipm.ctIsartMenu_UI)

    return project_name
