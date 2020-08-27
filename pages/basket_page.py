from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def verify_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT)
        assert message.text in "Your basket is empty. Continue shopping"

    def verify_empty_basket_items_list(self):
        basket_items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEM_ROW)
        assert len(basket_items) == 0, "There are some items in basket list"

