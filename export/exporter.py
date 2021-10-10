import os

from CommonTools.concat import concat
from CommonTools.os_ import make_dirs
from Maya.common_ import export_alembic, get_root_for_abc_export, smooth_selection, undo, get_objects, \
    get_cam_for_abc_export, frame_range

try:
    PATH = os.environ["ITEM_PUBLISH"]
    NAME = os.environ["ITEM_NAME"]
    TASK = os.environ["ITEM_TASK"]
except KeyError:
    raise RuntimeError("No scene loaded")


class Core:

    START_FRAME, END_FRAME = frame_range()

    @staticmethod
    def compute_export_path(comment=""):

        if comment in [None, ""]:
            filename = concat(NAME, TASK, separator="_")
            path = os.path.join(PATH, NAME, TASK).replace("\\", "/")
        else:
            filename = concat(NAME, TASK, comment, separator="_")
            path = os.path.join(PATH, NAME, TASK, comment).replace("\\", "/")

        make_dirs(path)

        filepath_ = concat(path, filename, separator="/")

        return filepath_

    @staticmethod
    def compute_hd_export(start_frame=1, end_frame=1):
        sel = get_objects(False)
        smooth_selection(sel)
        filepath = Core.compute_export_path(comment="HD")

        Core.export_abc(filepath, start_frame, end_frame)

        undo()

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
