from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[class*='add-to-basket']")
    ITEM_NAME_IN_CONF_MSG = (By.CSS_SELECTOR, "div[id='messages']>div:nth-of-type(1)>div>strong")
    ITEM_NAME_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main>p[class='price_color']")
    ITEM_PRICE_IN_CONF_MSG = (By.CSS_SELECTOR, "div[id='messages']>div:nth-of-type(3)>div>p>strong")



