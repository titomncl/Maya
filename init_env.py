# version: 1.1.0

def main():

    import os
    import sys

    import maya.cmds as cmds

    print("INIT_ENV")

    if os.path.isdir("E:/DEV"):
        dev = True
    else:
        dev = False

    ROOT_PATH = pfe_root_path(dev)

    if ROOT_PATH:
        project_name = ipm_package(ROOT_PATH, dev)

        PFE_ENV = ROOT_PATH + "/" + project_name

        DEV_ENV = "E:/DEV"

        if os.path.isdir(DEV_ENV):
            PFE_ENV = "D:/"
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


def pfe_root_path(dev=False):
    import os

    google_path = "G:/.shortcut-targets-by-id/1LKqbnGUt5-Lrfl9lElekEI0vY2DOIoog/"
    school_path = "X:/INPUT/"

    if dev:
        return "D:/"

    if os.path.isdir(google_path + "VSPA/DATA/LIB/CHARA"):
        return google_path
    elif os.path.isdir(school_path + "VSPA/DATA/LIB/CHARA"):
        return school_path
    else:
        print("No PFE path found.")
        return None


def ipm_package(path, dev=True):

    import sys

    print("IPM path is:", path)
    print("Dev mode:", dev)

    if dev:

        ############ ADD IPM IN PYTHONPATH ############
        ipm_path = "E:/DEV"
        sys.path.append(ipm_path + "/ISART_PROJECT_MANAGER/")
        sys.path.append(ipm_path + '/ISART_PROJECT_MANAGER/PY/')

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

        ############ ADD IPM IN PYTHONPATH ############
        ipm_path = path + "/VSPA/DEV/main"
        sys.path.append(ipm_path + "/ISART_PROJECT_MANAGER/")
        sys.path.append(ipm_path + '/ISART_PROJECT_MANAGER/PY/')

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
