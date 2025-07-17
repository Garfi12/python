from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
search_field = "#username"
search_input_username = driver.find_element(By.XPATH, '//*[@id="username"]')
search_input_username.send_keys("tomsmith")
search_input_password = driver.find_element(By.XPATH, '//*[@id="password"]')
search_input_password.send_keys("SuperSecretPassword!")
search_input = driver.find_element(By.XPATH, '//*[@id="login"]/button')
search_input.click()
sleep(3)