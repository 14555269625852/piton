import pytest
import requests
from lesson_8.URL import URL_X_client


@pytest.fixture()
def get_token(username='bloom', password='fire-fairy'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(URL_X_client + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
