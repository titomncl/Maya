from Maya.common_ import get_main_window, kill_instance
from qtpy.QtWidgets import QWidget
from qtpy.QtCore import Qt

class UI(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        title = "Rename Tool"
        kill_instance(get_main_window(), title)

        self.setWindowFlag(Qt.Tool)
        self.setParent(parent)
        self.setWindowTitle(title)

        self.set_ui()
        self.show()

    def set_ui(self):

        self.setFixedSize(400,200)

    def closeEvent(self, _):
        self.destroy()


def main():
    from Maya.common_ import get_main_window

    maya_ui = get_main_window()
    _ = UI(maya_ui)
