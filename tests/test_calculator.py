import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator = CalculatorPage(self.driver)
        yield
        self.driver.quit()
        
    def test_calculator_with_delay(self):
        self.calculator.set_delay("45")
        self.calculator.click_button("7")
        self.calculator.click_button("+")
        self.calculator.click_button("8")
        self.calculator.click_button("=")
        
        result = self.calculator.get_result(50)  # 50 секунд таймаут
        assert result == "15", f"Expected 15, but got {result}"