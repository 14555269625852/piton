from lesson_9.employee import Employer
from lesson_9.URL import URL_X_client, SQL
from lesson_9.data import DataBase
import allure


employer = Employer(URL_X_client)
db = DataBase(SQL)


@allure.epic("x-clientc")
@allure.severity(severity_level="normal")
@allure.title("Список сотрудников")
@allure.description("Получить список сотрудников из БД и АПИ, после чего сравнить их")
@allure.feature('Тест 1')
def test_get_list_employer():
    with allure.step("Создать компанию в БД"):
        db.create_company('sveta', 'list')
    with allure.step("Получить ID последней созданной компании"):
        max_id = db.max_company_id()
    with allure.step("Добавить сотрудника в БД"):
        db.create_employee(max_id, "Sveta", "YUSHKOVA", "89999999999")
    with allure.step("получить список сотрудников изпоследней созданной компании -БД"):
        db_employer_list = db.get_employee_list(max_id)
    with allure.step("получить список сотрудников изпоследней созданной компании -АПИ"):
        api_employer_list = employer.get_list(max_id)
    with allure.step("Получить список сотрудников полученных из БД и проверить, что он не пустой"):
        assert db_employer_list is not None
    with allure.step("Получить список сотрудников полученныхи через АПИ и проверить, что он не пустой"):
        assert api_employer_list is not None
    with allure.step("Сравнить списки сотрудников полученныхиз БД и АПИ"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("Удалить созданного сотрудника из БД"):
        response = (employer.get_list(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("Удалить последню созданную компанию из БД"):
        db.delete_company(max_id)


@allure.epic("x-clientc")
@allure.severity(severity_level="critical")
@allure.title("Добавить нового сотрудника")
@allure.description("Добавить нового сотрудника в БД и сравнить с АПИ Имя, проверить что ID сотрудника не пустой и строковый")
@allure.feature('Тест 1')
def test_add_new_employee():
    with allure.step("Создать компанию в БД"):
        db.create_company('sveta111', 'new')
    with allure.step("Получить ID последней созданной компании"):
        max_id = db.max_company_id()
    with allure.step("Добавить сотрудника в БД"):
        db.create_employee(max_id, "sveta", "YUSHKOVA", "89999999999")
    with allure.step("Получить список сотрудников из последней созданной компании -АПИ"):
        response = (employer.get_list(max_id))[0]
    with allure.step("Получить ID сотрудника"):
        employer_id = response['id']
    with allure.step("Получить ID созданного сотрудника из БД и проверить, что он не пустой и строковый"):
        assert employer_id is not None
        assert str(employer_id)
    with allure.step("Получить список сотрудников полученныхиз БД И АПИ и сравнить Имя"):
        assert response["firstName"] == "sveta"
    with allure.step("Удалить созданного сотрудника из БД"):
        db.delete_employer(employer_id)
    with allure.step("Удалить последню созданную компанию из БД"):
        db.delete_company(max_id)


@allure.epic("x-clientc")
@allure.severity(severity_level="critical")
@allure.title("Получить сотрудника по ID")
@allure.description("Получить сотрудника по ID в БД и проверить что ID сотрудника не пустой и строковый")
@allure.feature('Тест 1')
def test_get_by_id():
    with allure.step("Создать компанию в БД"):
        db.create_company('sveta222', 'by_id')
    with allure.step("Получить ID последней созданной компании"):
        max_id = db.max_company_id()
    with allure.step("Добавить сотрудника в БД"):
        db.create_employee(max_id, "sveta", "YUSHKOVA", "89999999999")
    with allure.step("Получить список сотрудников из последней созданной компании из БД"):
        employer_id = db.get_employee_id(max_id)
    with allure.step("Получить список сотрудников изпоследней созданной компании -АПИ"):
        get_api = (employer.get_list(employer_id))
    with allure.step("Получить ID сотрудника из БД и проверить, что он не пустой и строковый"):
        assert get_api is not None
        assert str(get_api)
    with allure.step("Удалить созданного сотрудника из БД"):
        db.delete_employer(employer_id)
    with allure.step("Удалить последню созданную компанию из БД"):
        db.delete_company(max_id)


@allure.epic("x-clientc")
@allure.severity(severity_level="critical")
@allure.title("Редактировать сотрудника")
@allure.description("Редактировать сотрудника  и проверить что измененная информация передалась и принимает строковое значение")
@allure.feature('Тест 1')
def test_edit_employee_info():
    with allure.step("Создать компанию в БД"):
        db.create_company('sveta222', 'by_id')
    with allure.step("Получить ID последней созданной компании"):
        max_id = db.max_company_id()
    with allure.step("Добавить сотрудника в БД"):
        db.create_employee(max_id, "sveta", "YUSHKOVA", "89999999999")
    with allure.step("Получить список сотрудников из последней созданной компании из БД"):
        employer_id = db.get_employee_id(max_id)
    with allure.step("Редактировать информацию о сотруднике в БД"):
        db.update_employee("SVETAedit", employer_id)
    with allure.step("Получить список сотрудников изпоследней созданной компании  через Апи"):
        get_api = (employer.get_list(employer_id))
    with allure.step("Проверить что измененная иформаия передалась и приняла строковое значение "):
        assert get_api is not None
        assert str(get_api)
    with allure.step("Удалить созданного сотрудника из БД"):
        db.delete_employer(employer_id)
    with allure.step("Удалить последню созданную компанию из БД"):
        db.delete_company(max_id)
