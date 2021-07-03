from CommonTools.save_load.controller import Controller
from Maya.save_load.save_load import SaveLoad
from Maya.common_ import get_main_window
from Maya.globals import ROOT_PATH, PROJECT


def main():

    instance = Controller(SaveLoad().load, "Load", get_main_window(), ROOT_PATH, PROJECT)
