from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.delay_field = (By.ID, "delay")
        self.result_field = (By.CLASS_NAME, "screen")
    
    def set_delay(self, delay: str) -> None:
        """Установка значения задержки."""
        delay_input = self.driver.find_element(*self.delay_field)
        delay_input.clear()
        delay_input.send_keys(delay)
    
    def press_button7(self) -> None:
        """Нажатие кнопки 7."""
        button = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button.click()
    
    def press_button8(self) -> None:
        """Нажатие кнопки 8."""
        button = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button.click()
    
    def press_button_plus(self) -> None:
        """Нажатие кнопки +."""
        button = self.driver.find_element(By.XPATH, "//span[text()='+']")
        button.click()
    
    def press_button_equals(self) -> None:
        """Нажатие кнопки =."""
        button = self.driver.find_element(By.XPATH, "//span[text()='=']")
        button.click()
    
    def get_result(self) -> str:
        """Получение результата вычислений."""
        return self.driver.find_element(*self.result_field).text