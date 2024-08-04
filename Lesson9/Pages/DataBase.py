from sqlalchemy import create_engine, text


class DataBase:
    query = {
        'create_company': text('insert into company (name, description) values (:name, :description)'),
        'max_company_id': text('select MAX(id) from company'),
        'delete_company': text('delete from company where id = :company_id'),
        'list_SELECT': text('select * from employee where company_id = :id'),
        'item_SELECT': text('select * from employee where company_id = :c_id and id = :e_id'),
        'maxID_SELECT': text('select MAX(id) from employee where company_id = :c_id'),
        'item_DELETE': text('delete from employee where id = :id_delete'),
        'item_UPDATE': text('update employee set first_name = :new_name where id = :employer_id'),
        'item_INSERT': text('insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone_num)')
    }


    def __init__(self):
        self.db = create_engine("postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx", echo=True)
        

    def execute_query(self, query_key, parameters=None):
        try:
                with self.db.connect() as connection:
                    result = connection.execute(self.query[query_key], parameters)
                    connection.commit()
                    self.db.connect()
                    return result
        except Exception as ex:
            print("Connection with BD error", ex)
        finally:
            connection.close()
            print("Connection is closed")

    def create_company(self, company_name: str, description: str):
        return self.execute_query('create_company', {'name': company_name, 'description': description})
    
    def delete_company(self, company_id: int):
        return self.execute_query('delete_company', {'company_id': company_id})
    
    def last_company_id(self):
        result = self.db.execute_query('max_company_id')
        return result.fetchall()[0][0]
 
    def get_employees_list(self, company_id: int):
        result = self.execute_query('list_SELECT', {'id': company_id})
        return result.fetchall()
    
    def create_employee(self, company_id: int, first_name: str, last_name: str, phone: str):
        return self.execute_query('item_INSERT', {'id': company_id, 'name': first_name, 'surname': last_name, 'phone_num': phone})
    
    def get_employee_id(self, company_id: int):
        result = self.execute_query('maxID_SELECT', {'c_id': company_id})
        return result.fetchall()[0][0]
    
    def update_employee_info(self, new_name: str, id: int):
        return self.execute_query('item_UPDATE', {'new_name': new_name, 'employer_id': id})
    
    def delete_employee(self, id: int):
        return self.execute_query('item_DELETE', {'id_delete': id})
    