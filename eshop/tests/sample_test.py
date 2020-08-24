from eshop.page_objects.base_page import BasePage
from eshop.page_objects.product_card_page import ProductCardPage
from eshop.page_objects.product_listing_page import ProductListingPage
from eshop.tests.base_test import BaseTest


class SampleTest(BaseTest):

    def test_positive(self):
        BasePage(self.driver).access_item("free")
        products = ProductListingPage(self.driver).order_by_price_desc().get_products()
        for index in range(2):
            ProductCardPage(self.driver, products[index]).add_to_card().close_modal()
        self.assertEqual(BasePage(self.driver).get_cart_amount(), "2")

    def test_negative(self):
        self.fail("Failed test for testing purpose")
