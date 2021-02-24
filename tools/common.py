import maya.cmds as mc


def get_filepath():
    """
    Return the location of the current file

    Returns:
        str: fullpath (dirname/basename.ext)

    """
    filepath = mc.file(q=True, sceneName=True)

    if filepath:

        return filepath

    else:
        raise RuntimeError("File not saved yet.")
