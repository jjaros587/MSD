from selenium.webdriver.common.by import By
from eshop.utils.page_factory import find_by
from eshop.utils.waiter import Waiter


class BasePage:

    items = {
        "free": "/volne-prodejne-leky"
    }

    cart_amount = find_by(By.ID, "js-cart-amount-desktop")
    navigation = find_by(By.ID, "js-main-nav")

    def __init__(self, driver):
        self.driver = driver
        self.waiter = Waiter(driver)

    def access_item(self, key):
        self.navigation().find_element(By.XPATH, "//a[@href='%s']" % self.items[key]).click()
        self.waiter.wait_for_page_load()

    def get_cart_amount(self):
        return self.cart_amount().text
