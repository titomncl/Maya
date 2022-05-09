from Maya.rename_tool.core import compute_new_name_obj, rename, rename_multi_obj
from Maya.common_ import get_objects


class Controller(object):
    def __init__(self, ui, parent=None):
        self.ui = ui(self, parent)

        self.ui.show()

    @property
    def selection(self):
        return get_objects(dag=False) or []

    def get_name(self, new_name, all=False):
        obj = self.selection
        if len(obj) == 1:
            return compute_new_name_obj(new_name, obj)
        elif len(obj) > 1:
            padding = len(str(len(obj) + 1)) + 1
            return compute_new_name_obj(new_name, obj[-1], "1".zfill(padding))
        else:
            return "No selection"

    def rename(self, new_name):
        obj = self.selection

        if len(obj) == 1:
            rename(obj[-1], compute_new_name_obj(new_name, obj[-1]))
        elif len(obj) > 1:
            rename_multi_obj(new_name, obj)
