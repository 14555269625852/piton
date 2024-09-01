from lesson_9.URL import URL_X_client
import requests
import json


class Employer:
    def __init__(self, url=URL_X_client):
        self.url = url

    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(self.url + '/employee', params=company)
        return response.json()

    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()

    def get_by_id(self, employee_id: int):
        response = requests.get(self.url + '/employee' + str(employee_id))
        return response

    def edit_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + '/employee' + str(employee_id),
                                  headers=headers, json=body)
        return response
