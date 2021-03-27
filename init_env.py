# version: 1.0.2

def main():
    update_ipm()
    import time
    time.sleep(3)

    print("IPM UPDATED")

    import os

    import maya.cmds as cmds

    print("INIT_ENV")

    ############ HOT-FIX ############
    os.environ["PFE_PROJET"] = "G:/.shortcut-targets-by-id/1LKqbnGUt5-Lrfl9lElekEI0vY2DOIoog/VSPA"
    ROOT_PATH = "G:/.shortcut-targets-by-id/1LKqbnGUt5-Lrfl9lElekEI0vY2DOIoog"

    DEV_ENV = "E:/DEV"

    project_name = ipm_package(os.path.isdir(DEV_ENV))

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
    print("DONE")
    ########## AUTO UDPATE ##########
    from Maya import common_

    common_.update_shelf()
    cmds.evalDeferred(common_.update_user_setup)


def ipm_package(dev=False):
    import sys
    import os

    ############ USER PROFILE ############
    USER_PATH = os.environ['USERPROFILE'].replace('\\', '/')

    ############ ADD IPM IN PYTHONPATH ############
    sys.path.append(USER_PATH + "/ISART_PROJECT_MANAGER/")
    sys.path.append(USER_PATH + '/ISART_PROJECT_MANAGER/PY/')

    import Vinci

    if dev:
        import ipm_v2 as ipm

        ### VARIABLES GENERALES ###
        project_name = ipm.ct_choose_project()

        if project_name:
            print('PROJECT_NAME: ' + project_name)

            chara = ipm.ct_find_assets(project_name, 'CHARA')
            print('CHARA_LISTS : %s' % ' '.join(chara))

            props = ipm.ct_find_assets(project_name, 'PROPS')
            print('PROPS_LISTS : %s' % ' '.join(props))

            ### MENU ISART ###
            import maya.cmds as cmds

            cmds.evalDeferred(ipm.ISART_Menu_UI)

        return project_name
    else:
        import ipm

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

            cmds.evalDeferred(ipm.ctIsartMenu_UI)

        return project_name


def update_ipm():
    import subprocess
    import os

    print("UPDATE IPM")

    DEV_ENV = "E:\\DEV"
    PFE_ENV = "G:\\.shortcut-targets-by-id\\1LKqbnGUt5-Lrfl9lElekEI0vY2DOIoog"
    not_shell = False

    if not os.path.isdir(DEV_ENV):
        DEV_ENV = PFE_ENV + "\\VSPA\\DEV\\main"
        not_shell = True

    updater_path = DEV_ENV + "\\update_ipm.bat"

    subprocess.Popen(
        '"' + updater_path + '"',
        shell=not_shell)
