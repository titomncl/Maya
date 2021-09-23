import os
import re

from CommonTools.concat import concat
from Maya.common_ import export_alembic, get_filepath, get_root_for_abc_export, raise_error
from Maya.globals import PROJECT_PATH


def info_from_filepath():
    path, filename = os.path.split(get_filepath())
    filename, _ = os.path.splitext(filename)

    filename_pattern = re.compile(r"^(?P<asset>[A-Z0-9_]+)_(?P<task>[A-Z]+)_(?P<version>\d{3})$")
    path_pattern = re.compile(r".+(?P<type>CHARA|PROPS|SET|FX).+")

    filename_match = filename_pattern.match(filename)
    path_match = path_pattern.match(path)

    if filename_match and path_match:
        filename_grp = filename_match.groupdict()
        path_grp = path_match.groupdict()

        asset_name = filename_grp["asset"]
        type_ = path_grp["type"]
        task = filename_grp["task"]

        return asset_name, type_, task



def compute_export_path(name_, type_, task_, ):
    filename = concat(name_, task_, "LD", separator="_")
    filepath_ = concat(PROJECT_PATH, "DATA/LIB/PUBLISH", type_, name_, task_, "LD", filename, separator="/")

    return filepath_


def export_abc(filepath, start_frame=1, end_frame=1):

    frame_range = "-frameRange {} {}".format(str(start_frame), str(end_frame))
    abc_param = "-uvWrite -writeColorSets -writeFaceSets -worldSpace -writeVisibility -autoSubd -writeUVSets"
    data_format = "-dataFormat ogawa"
    root = get_root_for_abc_export()

    if not root:
        raise_error("No meshes to export")

    command = "{} {} {} {} {}.abc".format(frame_range, abc_param, data_format, root, filepath)
    print(command)
    # export_alembic(command)
