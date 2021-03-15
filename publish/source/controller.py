from qtpy.QtWidgets import QWidget as Qw

from Maya.publish.source import core
from Maya.globals import PROJECT

import ipm_v2

class Controller(object):

    def __init__(self, ui, parent=None):

        self.filepath = core.filepath()

        self.ui = ui(self, parent)

        self.first_save_or_not()

        self.asset_type = "CHARA"
        self.asset_name = ""
        self.dpt = "MOD"

        self.chara_btn = self.ui.chara_btn
        self.props_btn = self.ui.props_btn
        self.mod_btn = self.ui.mod_btn
        self.shd_btn = self.ui.shd_btn
        self.rig_btn = self.ui.rig_btn
        self.save_btn = self.ui.save_btn
        self.close_btn = self.ui.close_btn

        self.library_box = self.ui.library_combobox
        self.get_chara()
        self.update_asset_name()

        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.mod_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.rig_btn.setChecked(False)

        self.init_btn_connections()

    def first_save_or_not(self):
        if not self.filepath:
            self.show()
        else:
            choice, save_choice = self.ui.message_box()

            if choice == save_choice:
                self.save_and_publish(first_save=False)

    def show(self):
        self.ui.show()

    def save_and_publish(self, first_save=True):
        if first_save:
            self.filepath = core.first_save(self.asset_type, self.asset_name, self.dpt)
        else:
            self.filepath = core.save(self.filepath)

        core.publish(self.filepath)

    def init_btn_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.mod_btn.clicked.connect(self.mod_action)
        self.shd_btn.clicked.connect(self.shd_action)
        self.rig_btn.clicked.connect(self.rig_action)

        self.library_box.currentTextChanged.connect(self.update_asset_name)

        self.save_btn.clicked.connect(self.save_and_publish)
        self.close_btn.clicked.connect(self.close_action)

    def get_chara(self):
        characters = ipm_v2.ct_find_assets(PROJECT, 'CHARA\\*')

        characters.sort()

        self.library_box.clear()
        self.library_box.addItems(characters)

    def chara_action(self):
        self.props_btn.setChecked(False)
        self.asset_type = "CHARA"
        self.get_chara()

    def get_props(self):
        props = ipm_v2.ct_find_assets(PROJECT, 'PROPS\\*')

        props.sort()

        self.library_box.clear()
        self.library_box.addItems(props)

    def props_action(self):
        self.chara_btn.setChecked(False)
        self.asset_type = "PROPS"
        self.get_props()

    def mod_action(self):
        self.shd_btn.setChecked(False)
        self.rig_btn.setChecked(False)

        self.dpt = "MOD"

    def shd_action(self):
        self.mod_btn.setChecked(False)
        self.rig_btn.setChecked(False)

        self.dpt = "SHD"

    def rig_action(self):
        self.shd_btn.setChecked(False)
        self.mod_btn.setChecked(False)

        self.dpt = "RIG"

    def update_asset_name(self):
        self.asset_name = self.library_box.currentText()

    def close_action(self):
        self.ui.close()
