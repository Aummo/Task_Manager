from typing import Dict, List, Optional
from ..domain.task import Task
from ..repositories.task_repository import TaskRepository

class InMemoryTaskRepository(TaskRepository):

    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def add(self, task: Task) -> None:
        self._tasks[task.id] = task

    def get_by_id(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    def list_all(self) -> List[Task]:
        return list(self._tasks.values())

    def remove(self, task_id: str) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def clear(self) -> None:
        self._tasks.clear()
