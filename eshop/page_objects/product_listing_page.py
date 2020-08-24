import time
from selenium.webdriver.common.by import By
from eshop.page_objects.base_page import BasePage


class ProductListingPage(BasePage):

    ordering = {
        "price_asc": "category-filter-2",
        "price_desc": "category-filter-3"
    }

    def __init__(self, driver):
        super().__init__(driver)

    def order_by_price_desc(self):
        self._order_by("price_desc")
        return self

    def order_by_price_asc(self):
        self._order_by("price_asc")
        return self

    def get_products(self):
        return self.driver.find_elements(By.XPATH, "//div[@data-at='product-preview']")

    def _order_by(self, condition):
        self.waiter.wait_for_element(3, (By.XPATH, "//a[@data-at='%s']" % self.ordering[condition])).click()
        self.waiter.wait_for_page_load()
        time.sleep(2)  # I know this is bad but I didn't have enough time to handle this issue




