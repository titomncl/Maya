import os

from Maya.common_ import get_root_for_abc_export, export_alembic


def export_abc(path, filename, start_frame, end_frame):

    frame_range = "-frameRange {} {}".format(str(start_frame), str(end_frame))
    abc_param = "-uvWrite -writeColorSets -writeFaceSets -worldSpace -writeVisibility -autoSubd -writeUVSets"
    data_format = "-dataFormat ogawa"
    root = get_root_for_abc_export()
    filepath = "-file {}".format(os.path.join(path, filename))

    command = "{} {} {} {} {}".format(frame_range, abc_param, data_format, root, filepath)

    export_alembic(command)
