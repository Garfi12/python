import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage, CheckoutOverviewPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_shopping_flow(driver):

    driver.get("https://www.saucedemo.com/")


    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Иван", "Петров", "123456")

    overview_page = CheckoutOverviewPage(driver)
    total = overview_page.get_total()
    assert total == "$58.29", f"Ожидалась сумма $58.29, получено {total}"