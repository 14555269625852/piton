from lesson_9.employee import Employer
from lesson_9.URL import URL_X_client, SQL
from lesson_9.data import DataBase


employer = Employer(URL_X_client)
db = DataBase(SQL)


def test_get_list_employer():
    db.create_company('sveta', 'list')
    max_id = db.max_company_id()
    db.create_employee(max_id, "Sveta", "YUSHKOVA", "89999999999")
    db_employer_list = db.get_employee_list(max_id)
    api_employer_list = employer.get_list(max_id)
    assert db_employer_list is not None
    assert api_employer_list is not None
    assert len(db_employer_list) == len(api_employer_list)
    response = (employer.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    db.delete_company(max_id)


def test_add_new_employee():
    db.create_company('sveta111', 'new')
    max_id = db.max_company_id()
    db.create_employee(max_id, "sveta", "YUSHKOVA", "89999999999")
    response = (employer.get_list(max_id))[0]
    employer_id = response['id']
    assert employer_id is not None
    assert response["firstName"] == "sveta"
    assert str(employer_id)
    db.delete_employer(employer_id)
    db.delete_company(max_id)


def test_get_by_id():
    db.create_company('sveta222', 'by_id')
    max_id = db.max_company_id()
    db.create_employee(max_id, "sveta", "YUSHKOVA", "89999999999")
    employer_id = db.get_employee_id(max_id)
    get_api = (employer.get_list(employer_id))
    assert get_api is not None
    assert str(get_api)
    db.delete_company(employer_id)
    db.delete_employer(max_id)


def test_edit_employee_info():
    db.create_company('Sveta333', 'edit')
    max_id = db.max_company_id()
    db.create_employee(max_id, "sveta", "YUSHKOVA", "89999999999")
    employer_id = db.get_employee_id(max_id)
    db.update_employee("SVETAedit", employer_id)
    get_api = (employer.get_list(employer_id))
    assert get_api is not None
    assert str(get_api)
    db.delete_company(employer_id)
    db.delete_employer(max_id)
