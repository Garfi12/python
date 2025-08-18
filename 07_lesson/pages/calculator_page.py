from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        
    def set_delay(self, delay):
        self.driver.find_element(*self.delay_field).clear()
        self.driver.find_element(*self.delay_field).send_keys(delay)
        
    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()
        
    def get_result(self, timeout):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_field, "")
        ).text