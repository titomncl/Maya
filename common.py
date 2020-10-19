import maya.cmds as mc

def get_filepath():
    """

    Returns:
        str, str, str: filepath, filename, extension

    """

    filepath = mc.file(q=True, sn=True)

    if filepath is not None:

        filename = os.path.basename(filepath)
        filepath = os.path.dirname(filepath)

        name, ext = os.path.splitext(filename)

        return filepath, name, ext
    else:
        return None
