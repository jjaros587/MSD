from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Waiter:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, delay, locator, context=None):
        context = context if context is not None else self.driver
        ignored_exceptions = (StaleElementReferenceException)
        return WebDriverWait(context, delay, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located(locator))

    def wait_for_page_load(self):
        self.wait_for_element(5, (By.XPATH, "//body[not(contains(@class,'loader'))]"))
