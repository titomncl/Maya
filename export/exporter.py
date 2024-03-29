import os

from CommonTools.concat import concat
from CommonTools.os_ import make_dirs
from Maya.common_ import export_alembic, get_root_for_abc_export, smooth_selection, undo, get_objects, \
    get_cam_for_abc_export, frame_range


class Core(object):

    START_FRAME, END_FRAME = frame_range()

    @property
    def path(self):
        try:
            return os.environ["ITEM_PUBLISH"]
        except KeyError:
            return ""

    @property
    def name(self):
        try:
            return os.environ["ITEM_NAME"]
        except KeyError:
            return ""

    @property
    def task(self):
        try:
            return os.environ["ITEM_TASK"]
        except KeyError:
            return ""

    def compute_export_path(self, comment=""):

        if comment in [None, ""]:
            filename = concat(self.name, self.task, separator="_")
            path = os.path.join(self.path, self.name, self.task).replace("\\", "/")
        else:
            filename = concat(self.name, self.task, comment, separator="_")
            path = os.path.join(self.path, self.name, self.task, comment).replace("\\", "/")

        make_dirs(path)

        filepath_ = concat(path, filename, separator="/")
        print(filepath_)
        return filepath_

    @staticmethod
    def compute_hd_export(start_frame=1, end_frame=1):
        sel = get_objects(False)
        smooth_selection(sel)
        filepath = Core.compute_export_path(Core(), comment="HD")

        Core.export_abc(filepath, start_frame, end_frame)

        undo(sel)

    @staticmethod
    def export_abc(filepath, start_frame=1, end_frame=1):

        frame_range = "-frameRange {} {}".format(str(start_frame), str(end_frame))
        abc_param = "-uvWrite -writeColorSets -writeFaceSets -worldSpace -writeVisibility -autoSubd -writeUVSets"
        data_format = "-dataFormat ogawa"

        if "CAMERA" in filepath:
            root = get_cam_for_abc_export()
        else:
            root = get_root_for_abc_export()

        if not root:
            raise RuntimeError("No meshes to export")

        command = "{} {} {} {} -file {}.abc".format(frame_range, abc_param, data_format, root, filepath)
        export_alembic(command)


def main():
    from CommonTools.exporter import controller
    from Maya.common_ import get_main_window


    instance_ = controller.Controller(Core, get_main_window())
    instance_.ui.show()