from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def verify_item_name_equals_name_in_conf_msg(self):
        item_name_in_conf_msg = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_CONF_MSG)
        item_name_from_product_page = self.browser.find_element(*ProductPageLocators.ITEM_NAME_ON_PRODUCT_PAGE)
        assert item_name_from_product_page.text == item_name_in_conf_msg.text, "item name is not equal on product page and in confitmation message"

    def verify_item_price_equals_price_in_conf_msg(self):
        item_price_in_conf_msg = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_CONF_MSG)
        item_price_on_product_page = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_ON_PRODUCT_PAGE)
        assert item_price_on_product_page.text == item_price_in_conf_msg.text, "item price is not equal on product page and in confitmation message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
