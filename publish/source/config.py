import os
from CommonTools.logger import Logger

USER_PROFILE = os.environ["userprofile"]
MAYA_ENV = "/Documents/maya/2019/scripts"
PFE_ENV = os.getenv("PFE_ENV")

# -----------------------------------------------

NAME = "Maya"

log = Logger(NAME)
