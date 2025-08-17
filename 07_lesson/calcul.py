from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class CalculatorPage:
    """Page Object для страницы калькулятора."""
    
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.button_locator_template = "//span[text()='{}']/ancestor::button"

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        """Устанавливает время задержки вычислений."""
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        """Нажимает указанную кнопку калькулятора."""
        locator = (By.XPATH, self.button_locator_template.format(button_text))
        self.driver.find_element(*locator).click()

    def get_result(self, timeout=45):
        """Возвращает результат вычислений с ожиданием."""
        WebDriverWait(self.driver, timeout + 1).until(
            lambda d: d.find_element(*self.result_display).text != ""
        )
        return self.driver.find_element(*self.result_display).text


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_with_delay(driver):
    """Тест проверяет работу калькулятора с задержкой."""
    # 1. Инициализация Page Object
    calculator = CalculatorPage(driver)

    # 2. Открытие страницы
    calculator.open()

    # 3. Установка задержки
    calculator.set_delay(45)

    # 4. Выполнение операции 7 + 8
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # 5. Проверка результата
    result = calculator.get_result()
    assert result == "15", f"Ожидался результат 15, получено {result}"