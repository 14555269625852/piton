from selenium import webdriver
from FormaPage import Auth
import allure


@allure.epic("Forma")
@allure.severity(severity_level="normal")
@allure.title("Заполнение формы")
@allure.description("Заполнить форму данными, отправить, получить результат о заполненных и незаполненных полей")
@allure.feature('Тест 2')
def test_auth_form():
    with allure.step("Открыть форму в браузере Firefox и заполнить поля"):
        driver = webdriver.Firefox()
        auth_page = Auth(driver)
        auth_page.submit_form(
            "Иван",
            "Петров",
            "Ленина, 55-3",
            "test@skypro.com",
            "+7985899998787",
            "",
            "Москва",
            "Россия",
            "QA",
            "SkyPro",)
    with allure.step("Получить информацию с полей формы, после её отправки"):
        auth_page.response_form()
        success_results, danger_results = auth_page.get_result()
    with allure.step("Проверить, что все классы элементов заполненных и не заполненых полей имеют значение"):
        success_class = "alert-success"
        danger_class = "alert-danger"
    for i in success_results:
        assert success_class in i
    for k in danger_results:
        assert danger_class in k
    with allure.step("Закрыть форму"):
        auth_page._driver.quit()
