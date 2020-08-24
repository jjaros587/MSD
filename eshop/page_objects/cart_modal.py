from selenium.webdriver.common.by import By
from eshop.page_objects.base_page import BasePage
from eshop.utils.page_factory import find_by


class CartModal(BasePage):

    modal = find_by(By.ID, "js-dynamic-modal", cacheable=True)

    def __init__(self, driver):
        super().__init__(driver)
        self._wait_for_modal(False)

    def close_modal(self):
        self.modal().find_element(By.ID, "js-prebasket-close").click()
        self._wait_for_modal(True)

    def _wait_for_modal(self, hidden):
        value = "true" if hidden else "false"
        self.waiter.wait_for_element(5, (By.XPATH, "//*[@id='js-dynamic-modal' and @aria-hidden='"+value+"']"), self.modal())
