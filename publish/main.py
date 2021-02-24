import sys

from qtpy import QtWidgets

from Maya.publish.source.ui import UI
from Maya.publish.source.controller import Controller

from Maya.common_ import get_main_window

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    UI_INSTANCE = Controller(UI, get_main_window())
    UI_INSTANCE.show()
    sys.exit(app.exec_())
