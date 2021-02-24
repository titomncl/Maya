
from qtpy import QtWidgets as Qw


class UI(Qw.QWidget):

    def __init__(self, controller, parent):

        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.setWindowTitle("Publisher")

        self.set_ui()

    def set_ui(self):

        self.setMinimumSize(400, 600)
