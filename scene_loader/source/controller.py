
from CommonTools.concat import concat

from Maya.scene_loader.source import core
from Maya.globals import PROJECT, USER_PATH
from Maya.common_ import open_file

try:
    import ipm_v2
except ImportError:
    import sys
    sys.path.append(USER_PATH + '/ISART_PROJECT_MANAGER/PY/')

    import ipm_v2


class Controller(object):

    def __init__(self, ui, parent=None):

        self.ui = ui(self, parent)

        self.asset_type = "CHARA"
        self.asset_name = ""
        self.dpt = "MOD"

        self.chara_btn = self.ui.chara_btn
        self.props_btn = self.ui.props_btn
        self.mod_btn = self.ui.mod_btn
        self.shd_btn = self.ui.shd_btn
        self.rig_btn = self.ui.rig_btn
        self.load_btn = self.ui.load_btn
        self.close_btn = self.ui.close_btn

        self.library_box = self.ui.library_combobox

        self.get_asset(self.asset_type)
        self.update_asset_name()

        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.mod_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.rig_btn.setChecked(False)

        self.init_btn_connections()

        self.show()

    def show(self):
        self.ui.show()

    def init_btn_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.mod_btn.clicked.connect(self.mod_action)
        self.shd_btn.clicked.connect(self.shd_action)
        self.rig_btn.clicked.connect(self.rig_action)

        self.library_box.currentTextChanged.connect(self.update_asset_name)

        self.load_btn.clicked.connect(self.load_action)
        self.close_btn.clicked.connect(self.close_action)

    def chara_action(self):
        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.asset_type = "CHARA"
        self.get_asset(self.asset_type)

    def props_action(self):
        self.props_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.asset_type = "PROPS"
        self.get_asset(self.asset_type)

    def get_asset(self, asset):
        assets = ipm_v2.ct_find_assets(PROJECT, asset)
        assets.sort()

        self.library_box.clear()
        self.library_box.addItems(assets)

    def mod_action(self):
        self.mod_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.rig_btn.setChecked(False)

        self.dpt = "MOD"

    def shd_action(self):
        self.shd_btn.setChecked(True)
        self.mod_btn.setChecked(False)
        self.rig_btn.setChecked(False)

        self.dpt = "SHD"

    def rig_action(self):
        self.rig_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.mod_btn.setChecked(False)

        self.dpt = "RIG"

    def update_asset_name(self):
        self.asset_name = self.library_box.currentText()

    def load_action(self):
        path = core.get_filepath(self.asset_type, self.asset_name, self.dpt)
        last_file = core.get_last_file(path)

        filepath = concat(path, last_file, separator="/")

        open_file(filepath)

        self.close_action()

    def close_action(self):
        self.ui.close()
