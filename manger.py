from task import Task

class Taskmanager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, desc=''):
        task = Task(title=title, desc=desc, id=self.next_id)
        self.next_id += 1
        self.tasks.append(task)
        print(f'Task added: {task.title} (ID: {task.id})')
        return task

    def del_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                removed_task = self.tasks.pop(i)
                print(f'Task deleted: {removed_task.title}')
                return removed_task
        print(f'Task with ID {task_id} not found')
        return None
    
    def list_task(self):
        if not self.tasks:
            print('No tasks found')
            return []
        for task in self.tasks:
            print(f"{task.id}. {task.title} - {task.desc}")
        return self.tasks.copy()
    

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
