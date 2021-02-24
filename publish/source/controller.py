
class Controller(object):

    def __init__(self, ui, parent=None):

        self.ui = ui(self, parent)

        self.show()

    def show(self):
        self.ui.show()
