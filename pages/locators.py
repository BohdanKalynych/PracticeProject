from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini>span>a")
    LOGIN_OR_REGISTER_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASS_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[class*='add-to-basket']")
    ITEM_NAME_IN_CONF_MSG = (By.CSS_SELECTOR, "div[id='messages']>div:nth-of-type(1)>div>strong")
    ITEM_NAME_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main>p[class='price_color']")
    ITEM_PRICE_IN_CONF_MSG = (By.CSS_SELECTOR, "div[id='messages']>div:nth-of-type(3)>div>p>strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-of-type(1)")


class BasketPageLocators():
    BASKET_IS_EMPTY_TEXT = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")
    BASKET_ITEM_ROW = (By.CSS_SELECTOR, ".basket-items>div[class=row]")






