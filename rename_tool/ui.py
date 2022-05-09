from qtpy.QtWidgets import QLabel, QWidget, QVBoxLayout, QCheckBox, QLineEdit, QHBoxLayout, QPushButton
from qtpy.QtCore import Qt


class UI(QWidget):
    def __init__(self, controller, parent=None):
        """

        Args:
            parent (QMainWindow):
        """
        QWidget.__init__(self, parent)

        self.setAttribute(Qt.WidgetAttribute.WA_QuitOnClose)

        self.setParent(parent)
        self.setWindowFlags(Qt.Tool)

        self.controller = controller

        self.main_layout()

    def main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        # -- Edit new name
        new_name_label = QLabel("New object name:")
        self.new_name = QLineEdit()
        self.new_name.textChanged.connect(self.update_line_edit)

        # -- Control new name
        ctrl_name_layout = QHBoxLayout()
        ctrl_name_layout.setContentsMargins(5, 5, 5, 5)

        ctrl_name_label = QLabel("Computed name:")
        self.new_name_ctrl = QLineEdit()
        self.new_name_ctrl.setReadOnly(True)

        ctrl_name_layout.addWidget(ctrl_name_label)
        ctrl_name_layout.addWidget(self.new_name_ctrl)

        # -- btn
        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(5, 5, 5, 5)

        self.rename_btn = QPushButton("Rename")
        self.close_btn = QPushButton("Close")

        self.rename_btn.clicked.connect(self.rename_action)
        self.close_btn.clicked.connect(self.close)

        btn_layout.addStretch(1)
        btn_layout.addWidget(self.rename_btn)
        btn_layout.addWidget(self.close_btn)

        # -- Add in layout
        main_layout.addWidget(new_name_label)
        main_layout.addWidget(self.new_name)
        main_layout.addLayout(ctrl_name_layout)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def update_line_edit(self):
        self.new_name_ctrl.setText(self.controller.get_name(self.new_name.text()))

    def rename_action(self):
        self.controller.rename(self.new_name.text())

# if __name__ == '__main__':
#     UI(get_main_window())