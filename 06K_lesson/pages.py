from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_add_buttons = {
            'Sauce Labs Backpack': (By.ID, 'add-to-cart-sauce-labs-backpack'),
            'Sauce Labs Bolt T-Shirt': (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'),
            'Sauce Labs Onesie': (By.ID, 'add-to-cart-sauce-labs-onesie')
        }
        self.cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_item_to_cart(self, item_name):
        self.driver.find_element(*self.item_add_buttons[item_name]).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, 'first-name')
        self.last_name_field = (By.ID, 'last-name')
        self.zip_code_field = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')

    def fill_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.total_label = (By.CLASS_NAME, 'summary_total_label')

    def get_total(self):
        return self.driver.find_element(*self.total_label).text.split()[-1]