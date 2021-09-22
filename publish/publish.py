import os

from CommonTools.concat import concat

from Maya.globals import PROJECT_PATH, MAYA_EXT
from Maya.common_ import get_filepath, save_as, clean_mode, import_ref_to_scene, open_file


def filepath():
    try:
        filepath_ = get_filepath()
        if PROJECT_PATH not in filepath_:
            return None
        return filepath_
    except RuntimeError:
        return None


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
        next_version_ = int(version) + 1
        next_version_ = str(next_version_).zfill(padding)

        return concat(name_file, next_version_, separator="_")
    else:
        e = concat(file_, " is incorrect.")
        raise ValueError(e)


def get_last_file(path):

    files = os.listdir(path)

    if files:

        maya_files = [f for f in files if MAYA_EXT in f]

        maya_files.sort()

        last_file = maya_files[-1]

        return last_file
    else:
        raise RuntimeError("No files found.")


def save():

    from Maya.save_load import save
    save.main()


def publish(filepath_):
    path, name = os.path.split(filepath_)

    publish_path = path.rsplit("/", 1)[0]
    publish_path = concat(publish_path, "PUBLISH", separator="/")

    name, ext = os.path.splitext(name)
    publish_name = name.rsplit("_", 1)[0] + ext

    publish_ = concat(publish_path, publish_name, separator="/")

    save_as(publish_)
    open_file(filepath_)


def save_and_publish():
    filepath_ = get_filepath()

    if filepath_:
        clean_mode()
        save()
        import_ref_to_scene()
        publish(get_filepath())
