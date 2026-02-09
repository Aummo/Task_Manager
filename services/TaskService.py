import uuid

from tornado.process import task_id

from domain.task import Task
from repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def _generate_id(self) -> str:
        return str(uuid.uuid4())


    def add_task(self,title:str,desc:str='') -> Task:
        task_id = self._generate_id()
        task = Task(task_id, title, desc)
        self._repository.add(task)
        return task

    def delete_task(self, task_id: str) -> bool:
        return self._repository.remove(task_id)

    def list_tasks(self):
        return self._repository.list_all()

    def clear_tasks(self):
        self._repository.clear()
