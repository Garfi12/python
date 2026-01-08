from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
    
    def add_item_to_cart(self, item_id: str) -> None:
        add_to_cart_button = (By.ID, f"add-to-cart-{item_id}")
        self.driver.find_element(*add_to_cart_button).click()
    
    def go_to_cart(self) -> None:
        self.driver.find_element(*self.cart_button).click()