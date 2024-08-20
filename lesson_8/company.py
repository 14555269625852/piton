from lesson_8.URL import URL_X_client
import requests


class Company:
    def __init__(self, url=URL_X_client):
        self.url = url

    def get_company_list(self, params_to_add=None):
        result_company_list = requests.get(
            self.url + "/company", params=params_to_add)
        return result_company_list.json()
