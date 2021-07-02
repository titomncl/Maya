import os

from CommonTools.concat import concat

from Maya.globals import PFE_PATH, ROOT_PATH, PROJECT, MAYA_EXT
from Maya.common_ import get_filepath, save_as, get_main_window


class SaveFile(object):

    def __init__(self):
        pass

    @property
    def root(self):
        return ROOT_PATH

    @property
    def project(self):
        return PROJECT

    @property
    def ui_instance(self):
        return get_main_window()

    @property
    def filepath(self):
        return self.__filepath()

    def __filepath(self):
        try:
            filepath_ = get_filepath()
            if PFE_PATH not in filepath_:
                return None
            else:
                return filepath_
        except RuntimeError:
            return None

    def save(self):
        path, _ = os.path.split(self.filepath)

        files = os.listdir(path)

        maya_files = [f for f in files if MAYA_EXT in files]

        maya_files.sort()

        last_file, _ = os.path.splitext(maya_files[-1])

        new_filename = self.next_version(last_file)
        new_filepath = concat(path, new_filename + MAYA_EXT, separator="/")

        save_as(new_filepath)

    @staticmethod
    def next_version(file_):
        """
        Get the next version from the given file
        Args:
            file_:

        Raises:
            ValueError: if the filename is not correct

        Returns:
            str: file with last version

        """
        split_file = file_.rsplit("_", 1)
        name_file = split_file[0]
        version = split_file[-1]
        padding = len(version)

        if version.isdigit():
            next_version = int(version) + 1
            next_version = str(next_version).zfill(padding)

            return concat(name_file, next_version, separator="_")
        else:
            e = concat(file_, " is incorrect.")
            raise ValueError(e)

    @staticmethod
    def first_save(type_, name_, task_):
        """

        Args:
            type_ (str): chara, props, set
            name_ (str): name of the asset
            task_ (str): department of the file: MOD, RIG, SHD

        Returns:
            str, str: versioned and published filepath

        """
        filename = concat(name_, task_, "001" + MAYA_EXT, separator="_")
        filepath = concat(PFE_PATH, "DATA/LIB", type_, name_, task_, "SCENE/VERSION", filename, separator="/")

        save_as(filepath)
