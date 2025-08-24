from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price_label = (By.CLASS_NAME, "summary_total_label")
    
    def fill_out_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
    
    def click_continue(self) -> None:
        self.driver.find_element(*self.continue_button).click()
    
    def get_total_price(self) -> str:
        return self.driver.find_element(*self.total_price_label).text