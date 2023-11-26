# todotask.py

class TodoTask:

    def __init__(self, task_name, task_description):
        self.name = task_name
        self.description = task_description
        self.done = False

    def get_name(self):
        return self.name
    
    def get_desc(self):
        return self.description

    def change_desc(self, new_desc):
        self.description = new_desc
    
    def mark_as_done(self):
        if self.done == False:
            self.done = True
        else: 
            self.done = False