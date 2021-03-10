from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc

from Maya.common_ import get_main_window


class UI(Qw.QWidget):
    def __init__(self, controller, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.setParent(get_main_window())
        self.setWindowFlags(Qc.Qt.Tool)

        self.controller = controller

        self.set_ui()

    def set_ui(self):

        self.setMinimumSize(300, 500)

        layout = Qw.QHBoxLayout()
        label = Qw.QLabel("TEST")

        layout.addWidget(label)

        self.setLayout(layout)

    def message_box(self):

        save_choice = Qw.QMessageBox.Save

        msg_box = Qw.QMessageBox(self)
        msg_box.setWindowTitle("Save")
        msg_box.setText("The file will be saved and published.")
        msg_box.setInformativeText("Do you want to continue?")
        msg_box.setStandardButtons(Qw.QMessageBox.Save | Qw.QMessageBox.Cancel)
        msg_box.setDefaultButton(Qw.QMessageBox.Save)

        choice = msg_box.exec_()

        return choice, save_choice
