import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_complete_purchase_flow(driver):
    # Инициализация страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Авторизация
    login_page.login_as_standard_user()

    # 2. Добавление товаров
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")

    # 3. Переход в корзину и оформление
    inventory_page.go_to_cart()
    cart_page.proceed_to_checkout()

    # 4. Заполнение информации
    checkout_page.fill_shipping_info("John", "Doe", "12345")

    # 5. Проверка итоговой суммы
    total = checkout_page.get_total_amount()
    assert total == "Total: $58.29", f"Expected total to be $58.29, got {total}"