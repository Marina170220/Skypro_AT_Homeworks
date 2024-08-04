import pytest
from Lesson9.Pages.Employee import Employee
from Lesson9.Pages.DataBase import DataBase

api = Employee("https://x-clients-be.onrender.com")
db = DataBase()
    


def test_get_list_of_employers():
    db.create_company('Test company', 'test')
    max_id = db.last_company_id()
    db.create_employee(max_id, "John", "Smith", "88002001111")
    db_employees_list = db.get_employees_list(max_id)
    api_employees_list = api.get_employees_list(max_id)
    assert len(db_employees_list) == len(api_employees_list)
    response = (api.get_employees_list(max_id))[0]
    employee_id = response['id']
    db.delete_employee(employee_id)
    db.delete_company(max_id)


def test_add_new_employer():
    db.create_company('New company', 'test')
    max_id = db.last_company_id()
    db.create_employee(max_id, "Anna", "White", "88002221111")
    response = (api.get_employees_list(max_id))[0]
    employer_id = response["id"]
    assert response["companyId"] == max_id
    assert response["firstName"] == "Anna"
    assert response["isActive"] == True
    assert response["lastName"] == "White"
    db.delete_employee(employer_id)
    db.delete_company(max_id)


def test_assertion_data():
    db.create_company('Another new company', 'test')
    max_id = db.last_company_id()
    db.create_employee(max_id, "Mary", "Black", "88003321111")
    employer_id = db.get_employee_id(max_id)
    get_api_info = (api.employee_info(employer_id)).json()
    assert get_api_info["firstName"] == "Mary"
    assert get_api_info["lastName"] == "Black"
    assert get_api_info["phone"] == "88003321111"
    db.delete_employee(employer_id)
    db.delete_company(max_id)


def test_update_user_info():
    db.create_company('Updated company', 'test')
    max_id = db.last_company_id()
    db.create_employee(max_id, "Elton", "John", "88899774455")
    employer_id = db.get_employee_id(max_id)
    db.update_employee_info("New", employer_id)
    get_api_info = (api.employee_info(employer_id)).json()
    assert get_api_info["firstName"] == "New"
    assert get_api_info["lastName"] == "John"
    assert get_api_info["isActive"] == True
    db.delete_employee(employer_id)
    db.delete_company(max_id)
    