from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def enter_username(self, username: str) -> None:
        self.driver.find_element(*self.username_field).send_keys(username)
    
    def enter_password(self, password: str) -> None:
        self.driver.find_element(*self.password_field).send_keys(password)
    
    def click_login(self) -> None:
        self.driver.find_element(*self.login_button).click()