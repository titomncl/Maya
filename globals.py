import os

USER_PATH = os.environ['USERPROFILE'].replace('\\', '/')
MAYA_ENV = "/Documents/maya/2019/scripts"
PFE_PATH = os.environ["PFE_ENV"]
DEV_PATH = os.environ["DEV_ENV"]
PROJECT = os.environ["PFE_PROJET"].split("/")[-1]
