import os
from datetime import datetime
from pathlib import Path
from unittest import TestCase
from eshop.utils.config_parser import ConfigParser
from eshop.utils.driver_factory import DriverFactory


class BaseTest(TestCase):

    def setUp(self):
        self.driver = DriverFactory().run(ConfigParser().get_driver())
        self.driver.get("https://www.pilulka.cz/")
        self.driver.maximize_window()

    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + self.id() + ".png"
                path = ConfigParser().get_report_params()['output'] + "\\screenshots\\" + filename
                Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
                self.driver.get_screenshot_as_file(path)
        self.driver.close()
