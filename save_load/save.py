from CommonTools.save_load.controller import Controller
from Maya.save_load.save_load import SaveLoad
from Maya.common_ import get_main_window


def main():
    save_load = SaveLoad()
    if save_load.filepath:
        save_load.save()
    else:
        instance = Controller(save_load.save, "Save", get_main_window(),
                              SaveLoad().root, SaveLoad().project, SaveLoad().buttons)

        instance.ui.fx_btn.setEnabled(False)
