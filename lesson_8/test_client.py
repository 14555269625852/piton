from lesson_8.company import Company
from lesson_8.employee import Employer
from lesson_8.URL import URL_X_client
from lesson_8.token import get_token


employer = Employer(URL_X_client)
company = Company(URL_X_client)


def company_id():
    get_token()
    get_company = company.get_company_list
    id_company = get_company["id"]
    yield id_company


def test_auth(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)


def test_get_company_list():
    company_id = company.get_company_list()
    print(company_id)
    assert print is not None
    assert str(print)


def test_get_employee_list():
    company_id = company.get_company_list()
    assert len(company_id) > 0
    assert company_id is not None


def test_add_new_employee(get_token):
    token = str(get_token)
    com_id = company.get_company_list()
    body_employee = {
        "id": 0,
        "firstName": "Svelana",
        "lastName": "Ushkova",
        "middleName": "string",
        "companyId": com_id,
        "email": "12345@mail.ru",
        "url": "string",
        "phone": "89999999999",
        "birthdate": "2024-08-14T17:02:49.235Z",
        "isActive": 'true'
    }
    new_employer_id = (employer.add_new(token, body_employee))
    assert new_employer_id is not None
    assert str(new_employer_id)


def test_add_new_employee_withut_token(get_token):
    token = get_token
    com_id = company.get_company_list()
    body_employee = {
        "id": 0,
        "firstName": "Svelana",
        "lastName": "Ushkova",
        "middleName": "string",
        "companyId": com_id,
        "email": "12345@mail.ru",
        "url": "string",
        "phone": "89999999999",
        "birthdate": "2024-08-14T17:02:49.235Z",
        "isActive": 'true'
    }
    new_employer = employer.add_new(token, body_employee)
    assert new_employer['error'] == 'Bad Request'


def test_add_new_employee_withut_body(get_token):
    token = str(get_token)
    body_emploee = {}
    new_employer = employer.add_new(token, body_emploee)
    assert new_employer['statusCode'] == 500


def test_get_by_id():
    id = company.get_company_list()
    by_id = employer.get_by_id(id)
    assert by_id is not None
    assert str(by_id)


def test_edit_employee_info(get_token):
    token = str(get_token)
    company_id = company.get_company_list()
    employee_body = {
        'id': 6,
        'firstName': 'Svetlana',
        'lastName': 'Yushkoa',
        'middleName': 'string',
        'companyId': company_id,
        'email': '12345@mail.ru',
        'url': 'string',
        'phone': '87654320987',
        'birthdate': '2024-08-14T17:02:49.235Z',
        'isActive': 'true',
        }
    new_id = (employer.add_new(token, employee_body))
    assert new_id is not None
