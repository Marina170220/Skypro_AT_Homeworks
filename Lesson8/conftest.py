import pytest
import requests
from Lesson8.urls import X_clients_URL


@pytest.fixture()
def get_token(user='musa', password='music-fairy'):
    auth_data = {'username': user, 'password': password}
    resp_token = requests.post(X_clients_URL + '/auth/login', json=auth_data)
    token = resp_token.json()['userToken']
    return token
