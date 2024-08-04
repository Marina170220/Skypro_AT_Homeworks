from Lesson8.Pages.Todo import Task

task = Task()


def test_todo():
    #Получение списка задач
    list = task.get_list()
    assert list.status_code == 200

    #Создание новой задачи
    params = {'title': 'Новая задача',
              'completed': 'false'}
    new_task = task.create_task(params)
    assert new_task is not None

    #Переименование задачи
    params = {'title': 'Измененная задача',
              'completed': 'false'}
    renamed_task = task.rename_task(new_task, params)
    assert renamed_task.json()['title'] == "Измененная задача"

    #Получение информации по созданной задаче
    task_info = task.get_task_info(new_task)
    assert task_info.json()['title'] == "Измененная задача"
    assert task_info.json()['id'] == new_task

    #Изменение статуса на "Выполнена"
    params = {'completed': 'true'}
    satus_completed = task.change_status(new_task, params)
    assert satus_completed == True

    #Отмена выполнения задачи
    params = {'completed': 'false'}
    satus_uncomleted = task.change_status(new_task, params)
    assert satus_uncomleted == False

    #Удаление задачи
    deleting = task.delete_task(new_task)
    assert deleting == 200
