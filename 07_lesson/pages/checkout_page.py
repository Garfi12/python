from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        
    def fill_shipping_info(self, first_name, last_name, zip_code):
        # Ждем загрузки страницы checkout
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        # Небольшая пауза для полной загрузки
        time.sleep(2)
        
        # Ждем, пока элементы станут кликабельными
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        
        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        
        zip_code_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "postal-code"))
        )
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)
        
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()
        
    def wait_for_overview(self):
        # Ожидаем появления контейнера итогов на шаге 2
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout_summary_container"))
        )
        
    def get_total_amount(self):
        # Ждем появления элемента с итоговой суммой на странице обзора
        self.wait_for_overview()
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
        
    def finish_checkout(self):
        # Нажимаем кнопку завершения и ждем страницу подтверждения
        self.wait_for_overview()
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )