from Maya import common

reload(common)

filepath = common.get_filepath()

if filepath is None:
    raise RuntimeError("Save your file before publishing")
else:
    print(filepath)
