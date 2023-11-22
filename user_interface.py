# user_interface.py

from database import DataBase

class UserInterface:

    def ui_start(self):
        run = True
        while(run):
            run = self.ui_promt()

    def ui_promt(self):
        action_select = int(input('Select action you want to do: || ONLY NUMBER || \n1. New To-do task \n2. Show all Tasks or Remove \n3. Exit program \n'))

        return self.input_handler(action_select)

        
    def input_handler(self, action):
        if action == 1: 
            self.new_task()
            return True
        elif action == 2:
            # print("Show all Tasks or Remove selected.")
            self.show_all_tasks()
            return True
        elif action == 3:
            print("Exit program selected.")
            return False
        return False

    def new_task(self):
        task_name = input("Input name for your todo task: ")
        task_desc = input("Input description for your todo task: ")

        DataBase.insert_new_task(task_name, task_desc)

    def show_all_tasks(self):
        i = 1
        print("Showing all Tasks: \n")
        for task in DataBase.tasks:
            print(F"{str(i)}. {task.name}")
            i += 1
        print("\nEnd of list.")