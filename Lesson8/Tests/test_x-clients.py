from Lesson8.Pages.Employee import Employee, Company
from Lesson8.urls import X_clients_URL

employee = Employee()
company = Company()


def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)


def test_get_company_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()


def test_add_employer(get_token): 
    token = str(get_token)
    company_id = company.last_active_company_id()
    employee_body = {
        'id': 0,
        'firstName': 'John',
        'lastName': 'Smith',
        'middleName': 'string',
        'companyId': company_id,
        'email': 'test@test.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2010-08-10T11:02:45.622Z',
        'isActive': 'true'
    }

    new_employee_id = (employee.add_new_employee(token, employee_body))['id']
    assert new_employee_id is not None
    assert str(new_employee_id).isdigit()

    new_eployee_info = employee.employee_info(new_employee_id)
    assert new_eployee_info.json()['id'] == new_employee_id
    assert new_eployee_info.status_code == 200


def test_add_employer_without_token():
    company_id = company.last_active_company_id()
    token = ''
    employee_body = {
        'id': 0,
        'firstName': 'John',
        'lastName': 'Smith',
        'middleName': 'string',
        'companyId': company_id,
        'email': 'test@test.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2010-08-10T11:02:45.622Z',
        'isActive': 'true'
    }
    new_employee = employee.add_new_employee(token, employee_body)
    assert new_employee['message'] == 'Unauthorized'


def test_add_employer_without_body(get_token):
    token = get_token
    employee_body = {}
    new_employee = employee.add_new_employee(token, employee_body)
    assert new_employee['message'] == 'Internal server error'
    

def test_get_employer():
    company_id = company.last_active_company_id()
    employees_list = employee.get_employees_list(company_id)
    assert isinstance(employees_list, list)
    assert employees_list[2] is not None


def test_get_employees_list_without_company_id():
    try:
        employee.get_employees_list()
    except TypeError as e:
        assert str(e) == "Employee.get_employees_list() missing 1 required positional argument: 'company_id'"


def test_get_employees_list_invalid_company_id():
    try:
        employee.get_employees_list('')
    except TypeError as e:
        assert str(e) == "Employee.get_employees_list() missing 1 required positional argument: 'company_id'"


def test_get_new_employee_info_without_employer_id():
    try:
        employee.employee_info()
    except TypeError as e:
        assert str(e) == "Employee.employee_info() missing 1 required positional argument: 'employee_id'"


def test_change_eployee_info(get_token):
    token = get_token
    company_id = company.last_active_company_id()
    employee_body = {
        'id': 0,
        'firstName': 'John',
        'lastName': 'Smith',
        'middleName': 'string',
        'companyId': company_id,
        'email': 'test@test.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2010-08-10T11:02:45.622Z',
        'isActive': 'true'
    }
    new_employee = employee.add_new_employee(token, employee_body)
    id = new_employee.get('id')
    change_body = {
        'lastName': 'White',
        'email': 'test_change@test.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
    }
    changed_employee = employee.change_employee(token, id, change_body)
    assert changed_employee.status_code == 200
    assert id == changed_employee.json()['id']
    assert changed_employee.json()['email'] == change_body['email']


def test_employee_without_parameters():
    try:
        employee.change_employee()
    except TypeError as e:
        assert str(
            e) == "Employee.change_employee() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"
