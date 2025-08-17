from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_add_button = "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name):
        locator = (By.XPATH, self.item_add_button.format(item_name))
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self):
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.split("$")[1]

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_saucedemo_checkout(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()

    assert cart_page.get_cart_items_count() == 3
    cart_page.proceed_to_checkout()
 
    checkout_page.fill_shipping_info("John", "Doe", "12345")

    total_amount = checkout_page.get_total_amount()
    assert total_amount == "58.29", f"Expected total $58.29, got ${total_amount}"