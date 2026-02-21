import uuid

from ..domain.task import Task



class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def _generate_id(self) -> str:
        return str(uuid.uuid4())


    def add_task(self,title:str,desc:str='') -> Task:
        task_id = self._generate_id()
        task = Task(task_id, title, desc)
        self.repository.add(task)
        return task

    def delete_task(self, task_id: str) -> bool:
        return self.repository.remove(task_id)

    def list_tasks(self):
        return self.repository.list_all()

    def clear_tasks(self):
        self.repository.clear()
