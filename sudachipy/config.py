import json
import os

SETTINGFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "resources/sudachi.json")
RESOURCEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "resources")


class _Settings(object):

    def __init__(self):
        self.is_active = False
        self.dict_ = {}

    def activate(self, path=SETTINGFILE, resource_path=None):
        with open(path, "r", encoding="utf-8") as f:
            self.dict_ = json.load(f)
        self.is_active = True
        if resource_path:
            global RESOURCEDIR
            RESOURCEDIR = resource_path

    def __getitem__(self, key):
        if self.is_active:
            return self.dict_[key]
        else:
            raise RuntimeError('call activate beforehand')

    def has(self, key):
        return key in self.dict_


settings = _Settings()
