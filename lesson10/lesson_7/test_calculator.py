from selenium import webdriver
from CalculatorPage import Calculator
import allure


@allure.epic("Calculaor")
@allure.severity(severity_level="normal")
@allure.title("Работа с калькулятором")
@allure.description("Поиск полей и ввод данных и вывод результата вычислений")
@allure.feature('Тест 2')
def test_calculator():
    with allure.step("Открыть калькулятор в браузере Firefox"):
        driver = webdriver.Firefox()
        calculator = Calculator(driver)
    with allure.step("Ввести в поле delay значение"):
        calculator.set_delay("45")
    with allure.step("Ввести значения для вычисления"):
        calculator.get_buttons()
        total = calculator.operation(7, 8, "+", 15)
    with allure.step("Сравнить ролученный результат"):
        assert total == "15"
    with allure.step("Закрыть калькулятор"):
        calculator._driver.quit()
