import requests
import json
from Lesson8.urls import X_clients_URL

employees_path = '/employee'
employee_path = '/employee/'
company_path = '/company'

class Company:
    def __init__(self, url=X_clients_URL):
        self.url = url

    #Получение Id последней активной компании из списка
    def last_active_company_id(self):
        params = {'active': 'true'}
        response = requests.get(self.url + company_path, params=params)
        return response.json()[-1].get('id')


class Employee:
    def __init__(self, url=X_clients_URL):
        self.url = url

    #Получение списка сотрудников
    def get_employees_list(self, company_id: int):
        company = {'company': company_id}
        emp_response = requests.get(self.url + employees_path, params=company)
        return emp_response.json()
    
    #Добавление сотрудника в компанию
    def add_new_employee(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + employees_path, headers=headers, json=body)
        return response.json()
       
    #Получение информации о сотруднике
    def employee_info(self, employee_id: int):
        response = requests.get(self.url + employee_path + str(employee_id))
        return response
    
    #Изменение информации о сотруднике
    def change_employee(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + employee_path + str(employee_id), headers=headers, json=body)
        return response
