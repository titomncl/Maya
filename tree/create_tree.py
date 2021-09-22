import os
import re
import maya.cmds as mc

from Maya.common_ import get_filepath
from CommonTools.concat import concat


class ProjectTree(object):
    def __init__(self, filepath=None):
        self._filepath = filepath or get_filepath()
        self._filename = self.filename
        self._asset = self.asset
        self._asset_type = self.asset_type

        self.create_group()

    @property
    def filepath(self):
        return self._filepath

    @property
    def filename(self):
        pattern = re.compile(r"^(?P<asset>[A-Z0-9_]+)_(?P<type>[A-Z]+)_(?P<version>\d{3})$")

        name_is_correct = pattern.match(os.path.splitext(os.path.split(self.filepath)[-1])[0])

        if name_is_correct:
            return name_is_correct.groupdict()
        else:
            return None

    @property
    def asset(self):
        return self.filename["asset"]

    @property
    def asset_type(self):
        return self.filename["type"]

    def create_group(self):
        if not self.type_grp:
            mc.group(empty=True, name=concat(self.asset, self.asset_type, "grp", separator="_"))
        if not self.main_grp:
            mc.group(empty=True, name=concat(self.asset, "grp", separator="_"))

        try:
            mc.parent(self.type_grp, self.main_grp)
        except RuntimeError:
            pass

    @property
    def type_grp(self):
        return mc.ls(concat(self.asset, self.asset_type, "grp", separator="_"))

    @property
    def main_grp(self):
        return mc.ls(concat(self.asset, "grp", separator="_"))


# if __name__ == '__main__':
#     tree = ProjectTree()
