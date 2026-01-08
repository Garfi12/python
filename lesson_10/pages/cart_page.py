from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
    
    def get_cart_item_count(self) -> int:
        items = self.driver.find_elements(*self.cart_items)
        return len(items)
    
    def click_checkout(self) -> None:
        self.driver.find_element(*self.checkout_button).click()