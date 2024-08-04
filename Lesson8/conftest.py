import pytest
import requests
from Lesson8.urls import X_clients_URL


@pytest.fixture()
def get_token(user='musa', password='music-fairy'):
    auth_data = {'username': user, 'password': password}
    resp_token = requests.post(X_clients_URL + '/auth/login', json=auth_data)
    token = resp_token.json()['userToken']
    return token


# @pytest.fixture()
# def get_companies_list():
#     param_true = {'active': 'true'}
#     resp_companies = requests.get(X_client_URL + '/company', params=param_true)
#     last_companies_id = resp_companies.json()[-1]['id']
#     return last_companies_id


# @pytest.fixture(scope="class")
# def add_new_employer(get_token, get_list_companies):
#     company_id = get_list_companies
#     token = str(get_token[0])
#     headers = {'x-client-token': token}
#     body_employer = {
#         'id': 0,
#         'firstName': 'Ivan',
#         'lastName': 'Petrov',
#         'middleName': 'string',
#         'companyId': company_id,
#         'email': 'test@mail.ru',
#         'url': 'string',
#         'phone': 'string',
#         'birthdate': '2023-08-14T11:02:45.622Z',
#         'isActive': 'true'
#     }
#     resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer)
#     id_new_employer = resp_add_new_employer.json()['id']
#     return id_new_employer, headers
