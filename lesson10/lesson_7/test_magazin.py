from selenium import webdriver
from MagazinPage import OnlineShop
import allure


@allure.epic("magazine")
@allure.severity(severity_level="Critical")
@allure.title("Офрмление покупки и сравнивание итоговой цены")
@allure.description("Добавить в корзину необходимые товары, проверить итоговую стоимость товаров при оформлении заказа")
@allure.feature('Тест 2')
def test_online_shop():
    with allure.step("Открыть магазин в браузере Firefox и добавить нужные позиции в корзинц"):
        driver = webdriver.Firefox()
        online_shop = OnlineShop(driver)
        online_shop.user_auth("standard_user", "secret_sauce")
        online_shop.get_info_and_buttons()
        online_shop.add_items_to_cart("Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie")
    online_shop.place_order("Светлана", "Юшкова", "123456")
    total = online_shop.get_result_price()
    with allure.step("Сравнить стоимость товаров в корзине c ожидаемым результатом"):
        assert total == "Total: $58.29"
    with allure.step("Закрыть магазин"):
        online_shop._driver.quit()
