import os

from CommonTools.concat import concat

from Maya.globals import PFE_PATH


def get_filepath(type_, name, task):

    filepath = concat(PFE_PATH, "DATA/LIB", type_, name, task, "SCENE/OLD", separator="/")

    return filepath


def get_last_file(path):

    files = os.listdir(path)

    if files:

        if "desktop.ini" in files:
            files.remove("desktop.ini")

        files.sort()

        last_file = files[-1]

        return last_file
    else:
        raise RuntimeError("No files found.")
