from sqlalchemy import create_engine
from sqlalchemy.sql import text

class DataBase:
    __scripts  = {
        'get_companies_list':'select * from company where deleted_at is Null',
        'select_only_active': 'select * from company where is_active = true and deleted_at is Null',
        'create_company': text('insert into company (name, description) values (:name, :description)'),
        'max_company_id': text('select MAX(id) from company'),
        'delete_company': text('delete from company where id = :company_id'),
        'list_SELECT': text('select * from employee where company_id = :id'),
        'item_SELECT': text('select * from employee where company_id = :c_id and id = :e_id'),
        'maxID_SELECT': text('select MAX(id) from employee where company_id = :c_id'),
        'item_DELETE': text('delete from employee where id = :id_delete'),
        'item_UPDATE': text('update employee set first_name = :new_name where id = :employee_id'),
        'item_INSERT': text('insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone_num)')
    }


    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)


    def get_companies_list(self):
        return self.__db.execute(self.__scripts['get_companies_list']).fetchall()

    def get_active_companies_list(self):
        return self.__db.execute(self.__scripts['select_only_active']).fetchall()

    def delete_company(self, company_id: int):
        return self.__db.execute(self.__scripts['delete_company'], company_id=company_id)

    def create_company(self, company_name: str, description: str):
        return self.__db.execute(self.__scripts['create_company'], name=company_name, description=description)

    def last_company_id(self):
        return self.__db.execute(self.__scripts['max_company_id']).fetchall()[0][0]
    

    def get_employees_list(self,id):
        return self.__db.execute(self.__scripts['list_SELECT'], company_id=id).fetchall()  
    
    def create_employee(self, company_id: int, first_name: str, last_name: str, phone: str):
        return self.__db.execute(self.__scripts['item_INSERT'], id=company_id, name=first_name, surname=last_name, phone_num=phone)
    
    def get_employee_id(self, company_id: int):
        return self.__db.execute(self.__scripts['maxID_SELECT'], c_id=company_id).fetchall()[0][0]
    
    def update_employee_info(self, new_name: str, id: int):
        return self.__db.execute(self.__scripts['item_UPDATE'], new_name=new_name, employee_id=id)
    
    def delete_employee(self, id: int):
        return self.__db.execute(self.__scripts['item_DELETE'], id_delete=id)
