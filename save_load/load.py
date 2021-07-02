from CommonTools.save_load.controller import Controller
from Maya.save_load.save_load import SaveLoad


def main():
    instance = Controller(SaveLoad(), "Load")
