import requests
import json
from Lesson8.urls import Todo_list_URL


class Task:
    def __init__(self, url=Todo_list_URL):
        self.url = url

    #Получение списка задач
    def get_list(self):
        response = requests.get(self.url)
        return response

    #Создание задачи и получение ее Id
    def create_task(self, params: json):
        response = requests.post(self.url, json=params)
        return response.json()['id']
    
    #Переименование задачи
    def rename_task(self, id: int, params: json):
        response = requests.patch(self.url + str(id), json=params)
        return response
    
    #Получение информации о задаче
    def get_task_info(self, id: int):
        response = requests.get(self.url + str(id))
        return response
    
    #Изменение статуса задачи
    def change_status(self, id: int, params: json):
        response = requests.patch(self.url + str(id), json=params)
        status = response.json()['completed']
        return status
    
    #Удаление задачи и получение статус-кода ответа
    def delete_task(self, id: int):
        response = requests.delete(self.url + str(id))
        code = response.status_code
        return code
    