# todotask.py

class TodoTask:

    def __init__(self, task_name, task_description):
        self.name = task_name
        self.description = task_description

    def get_name(self):
        return self.name
    
    def get_desc(self):
        return self.description

    def change_description(self, new_desc):
        self.description = new_desc