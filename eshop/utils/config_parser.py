import os
import sys

import yaml
from eshop.utils.singleton import singleton


@singleton
class ConfigParser:

    config = None

    def __init__(self, config_path='config.yaml'):
        with open(os.path.join(os.path.dirname(sys.modules['__main__'].__file__), config_path)) as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

    def get_driver(self):
        return self.config['driver']

    def get_report_params(self):
        return self.config['report']
