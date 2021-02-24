import os

from Maya.tools import common

from Maya.publish.source.config import PFE_ENV

from Maya.publish.source.config import log


class Publish(object):

    def __init__(self):

        try:
            self.filepath = common.get_filepath()

            if self.filepath:
                filepath, name, ext = self.filepath
                print(filepath, name, ext)
        except RuntimeError:
            self.first_save()

    def first_save(self):
        print(PFE_ENV)
