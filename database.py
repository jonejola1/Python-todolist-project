# database.py

from todotask import TodoTask

class DataBase:

    tasks = []

    def insert_new_task(task_name, task_description):
        task = TodoTask(task_name, task_description)
        print(F'Succesfully added "{task.get_name()}" task')
        print(F"The description is {task.get_desc()}\n")
        
        DataBase.tasks.append(task)
        