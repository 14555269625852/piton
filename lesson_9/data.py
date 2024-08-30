from sqlalchemy import create_engine
from sqlalchemy.sql import text


class DataBase:
    query = {
        'create_company': text('insert into company (name, description) values (:name, :description)'),
        'delete_company': text('delete from company where id = :company_id'),
        'max_company_id': text('select MAX(id) from company'),
        'select_employee_list': text('select * from employee where company_id = :id'),
        'item_INSERT': text('insert into employee(company_id, first_name,  last_name, phone) values(:id, :name, :surname, :phone_num)'),
        'maxID_Select': text('select MAX(id) from employee where company_id = :c_id'),
        'update_employee': text('update employee set first_name = :new_name where id = :employer_id'),
        'delete_employee': text('delete from employee where id = :id_delete')
    }

    def __init__(self, engine):
        self.db = create_engine(engine)

    def execute_query(self, query_key, parameter=None):
        with self.db.connect() as connection:
            result = connection.execute(self.query[query_key], parameter)
            connection.commit()
            return result

    def create_company(self, company_name: str, description: str):
        return self.execute_query('create_company', {
            'name': company_name, 'description': description})

    def delete_company(self, company_id: int):
        return self.execute_query('delete_company', {'company_id': company_id})

    def max_company_id(self):
        result = self.execute_query('max_company_id')
        return result.fetchall()[0][0]

    def get_employee_list(self, company_id: int):
        result = self.execute_query('select_employee_list', {'id': company_id})
        return result.fetchall()

    def create_employee(self, company_id: int, first_name: str,
                        last_name: str, phone: str):
        return self.execute_query('item_INSERT', {
            'id': company_id, 'name': first_name, 'surname': last_name,
            'phone_num': phone})

    def get_employee_id(self, company_id: int):
        result = self.execute_query('maxID_Select', {'c_id': company_id})
        return result.fetchall()[0][0]

    def update_employee(self, new_name: str, id: int):
        return self.execute_query('update_employee', {
            'new_name': new_name, 'employer_id': id})

    def delete_employer(self, id: int):
        return self.execute_query('delete_employee', {'id_delete': id})
