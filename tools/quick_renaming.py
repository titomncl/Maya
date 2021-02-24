import re
import maya.cmds as mc

from CommonTools.concat import concat


def get_selection():
    sel = mc.ls(sl=True)
    return sel


def prompt(msg="New object name"):
    result = mc.promptDialog(title='Rename Object', message=msg, button=['OK', 'Cancel'],
                             defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')

    if result == 'OK':
        value = mc.promptDialog(query=True, text=True)
        return value
    else:
        return None


def check_input(value):
    name_re = re.compile(r"^[A-Za-z0-9]+$")

    long_name_re = re.compile(r"(?P<asset>[A-Z]+)_(?P<side>[CLR])_(?P<object>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)([0-9]+)?")

    name_is_correct = name_re.match(value)
    long_name_is_correct = long_name_re.match(value)

    print(value, long_name_is_correct)

    if name_is_correct:
        return value, False
    elif long_name_is_correct:
        return value, long_name_is_correct
    else:
        return None


def rename_object(sel, value):

    new_object_name, is_long_name = value

    for count, object_name in enumerate(sel):

        if is_long_name:
            dict_name = is_long_name.groupdict()
            name = dict_name["object"]

        else:
            regex = re.compile(r"(?P<asset>[A-Z]+)_(?P<side>[CLR])_(?P<object>[A-Za-z0-9]+)_(?P<type>[A-Za-z]+)([0-9]+)?")

            name_is_correct = regex.match(object_name)

            dict_name = name_is_correct.groupdict()

            name = new_object_name

        if len(sel) > 1:
            iteration = str(count + 1).zfill(2)
        else:
            iteration = ""

        new_name = concat(dict_name["asset"], dict_name["side"], name + iteration, dict_name["type"],
                          separator="_")

        mc.rename(object_name, new_name)


def main():

    value = prompt()

    if value:
        checked = check_input(value)

        selection = get_selection()

        while not checked:
            if value == "" or len(selection) == 0:
                break
            else:
                value = prompt("Name is not conform. Should be letters and/or numbers.")
                checked = check_input(value)

        rename_object(selection, checked)
