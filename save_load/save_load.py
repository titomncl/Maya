import os
import sys

if sys.version_info > (3,):
    import typing

    if typing.TYPE_CHECKING:
        from Odin import Asset, Shot
        from typing import Optional, Union

from collections import OrderedDict

from CommonTools.concat import concat
from CommonTools.os_ import glob_path_recursive
from Maya.common_ import get_filepath, save_as, open_file
from Maya.globals import PROJECT_PATH, ROOT_PATH, PROJECT, MAYA_EXT
from Maya.tree.create_tree import ProjectTree


class SaveLoad(object):

    @property
    def root(self):
        return ROOT_PATH

    @property
    def project(self):
        return PROJECT

    @property
    def filepath(self):
        try:
            filepath_ = get_filepath()
            if PROJECT_PATH not in filepath_:
                return None
            else:
                return filepath_
        except RuntimeError:
            return None

    @property
    def buttons(self):
        buttons = OrderedDict()

        buttons["Assets"] = ["MOD", "SHD", "RIG"]

        buttons["Shots"] = ["ANIMATION", "LAYOUT", "LIGHTING", "COMPOSITING", "FX"]

        return buttons

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

    def file_to_load(self, path):

        last_file = self.get_last_file(path)

        filepath = concat(path, last_file, separator="/")

        return filepath

    @staticmethod
    def get_last_file(path):

        files = os.listdir(path)

        if files:

            maya_files = [f for f in files if MAYA_EXT in f]

            maya_files.sort()

            last_file = maya_files[-1]

            return last_file
        else:
            raise RuntimeError("No files found.")

    def save(self, item="", dpt=""):
        # type: (Optional[Union[Asset, Shot]], str) -> None
        """.
        Args:
            item: name of the asset
            dpt: department of the file: MOD, RIG, SHD

        """
        if self.filepath:
            path, _ = os.path.split(self.filepath)

            file_ = self.get_last_file(path)

            last_file, _ = os.path.splitext(file_)

            new_filename = self.next_version(last_file)
            new_filepath = concat(path, new_filename + MAYA_EXT, separator="/")

            ProjectTree()

            save_as(new_filepath)
        else:
            path = os.path.join(item.paths["PATH"], item.name, dpt).replace("\\", "/")
            path = glob_path_recursive(path, "VERSION")

            filename = concat(item.name, dpt, "001" + MAYA_EXT, separator="_")
            filepath_ = concat(path, filename, separator="/")

            ProjectTree(filepath_)

            save_as(filepath_)

    def load(self, item, dpt):
        path = os.path.join(item.paths["PATH"], item.name, dpt).replace("\\", "/")

        path = glob_path_recursive(path, "VERSION")

        file_ = self.file_to_load(path)

        open_file(file_)
