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
        if not DataBase.tasks: 
            print("There are no tasks.")
            return
        
        i = 1
        print("Showing all Tasks: \n")
        for task in DataBase.tasks:
            print(F"{str(i)}. {task.name}")
            i += 1
        # print("\nEnd of list.\n What task do you want to change: ")
        user_input = int(input("\nEnd of list.\n What task do you want to change: "))
        self.task_command(user_input)


    def task_command(self, user_input):
        print(F'Task Name: "{DataBase.tasks[user_input-1].get_name()}" Task Description: "{DataBase.tasks[user_input-1].get_desc()}"')
        user_action = int(input("\n1. Mark as done \n2. Change description\n3. Delete \n4. Cancel "))
        if user_action == 1:
            print("Mark as done")
            return
        if user_action == 2:
            new_desc = input("Enter new description: ")
            DataBase.tasks[user_input - 1].change_desc(new_desc)
            print(F'New description changed to "{new_desc}"')
            return
        if user_action == 3:
            print(F'Removing task "{DataBase.tasks[user_input-1].get_name()} from the list.')
            DataBase.tasks.pop(user_input - 1)
            print("Task removed!")
            return
        if user_action == 4:
            print("Cancelled")
            self.task_command(user_input)
