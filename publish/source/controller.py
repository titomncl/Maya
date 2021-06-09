from Maya.publish.source import core
from Maya.common_ import clean_mode

try:
    import ipm_v2
except ImportError:
    import sys
    sys.path.append(USER_PATH + '/ISART_PROJECT_MANAGER/PY/')

    import ipm_v2

class Controller(object):

    def __init__(self):

        self.filepath = core.filepath()

        self.save_and_publish()

    def save_and_publish(self):
        clean_mode()
        self.filepath = core.save(self.filepath)
        core.publish(self.filepath)
