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
        # Ждем, пока элемент появится
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.result_field)
        )
        
        # Ждем, пока результат изменится (появится число вместо выражения)
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_text = element.text
            # Если текст содержит только цифры (результат вычисления)
            if current_text.isdigit():
                return current_text
            time.sleep(0.5)
        
        # Если таймаут истек, возвращаем текущий текст
        return element.text