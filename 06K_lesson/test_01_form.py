import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_validation():
    
    driver = webdriver.Edge()
    
    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        # Заполнение формы
        driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
        
        # Нажатие кнопки Submit
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
        # Даем время для применения стилей (можно заменить на явное ожидание)
        time.sleep(1)
        
      
        zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code')
        assert "is-invalid" in zip_code.get_attribute("class")
        
       
        valid_fields = [
            'first-name',
            'last-name',
            'address',
            'e-mail',
            'phone',
            'city',
            'country',
            'job-position',
            'company'
        ]
        
      
        for field in valid_fields:
            element = driver.find_element(By.CSS_SELECTOR, f'#{field}')
            assert "is-valid" in element.get_attribute("class"), f"Поле {field} не валидно"
            
    finally:
      
        driver.quit()

if __name__ == "__main__":
    test_form_validation()