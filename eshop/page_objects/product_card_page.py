from selenium.webdriver.common.by import By
from eshop.page_objects.base_page import BasePage
from eshop.page_objects.cart_modal import CartModal


class ProductCardPage(BasePage):

    def __init__(self, driver, product):
        super().__init__(driver)
        self.button_add_to_cart = self.waiter.wait_for_element(15, (By.CLASS_NAME, "js-amount-zero"), product)

    def add_to_card(self):
        self.button_add_to_cart.click()
        self.waiter.wait_for_page_load()
        return CartModal(self.driver)
