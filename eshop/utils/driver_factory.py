from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from eshop.utils.singleton import singleton


@singleton
class DriverFactory:

    allowed_drivers = ["chrome"]

    def run(self, driver_name):
        if driver_name not in self.allowed_drivers:
            raise ValueError("%s is not one of the allowed drivers. Valida drivers are %s" % (driver_name, str(self.allowed_drivers)))
        if driver_name == "chrome":
            return webdriver.Chrome(executable_path=ChromeDriverManager().install())
