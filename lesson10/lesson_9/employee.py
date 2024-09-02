from lesson_9.URL import URL_X_client
import requests
import json
import allure


class Employer:
    def __init__(self, url=URL_X_client):
        self.url = url

    @allure.step("Получить список сотрудников компании по ID")
    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(self.url + '/employee', params=company)
        return response.json()

    @allure.step("Добавить нового сотрудника")
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()

    @allure.step("Получить информацию о сотруднике по ID")
    def get_by_id(self, employee_id: int):
        response = requests.get(self.url + '/employee' + str(employee_id))
        return response

    @allure.step("Редактировать информацию о сотруднике")
    def edit_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + '/employee' + str(employee_id),
                                  headers=headers, json=body)
        return response
