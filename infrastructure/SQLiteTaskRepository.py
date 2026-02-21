
import sqlite3
from typing import Optional

from ..repositories.task_repository import TaskRepository
from ..domain.task import Task

class SQLiteTaskRepository(TaskRepository):

    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT
            )
        """)
        self.conn.commit()

    def add(self, task):
        self.cursor.execute(
            "INSERT INTO tasks (id, title, description) VALUES (?, ?, ?)",
            (task.id, task._title, task._desc)
        )
        self.conn.commit()

    def get_by_id(self, task_id: str) -> Optional[Task]:
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()
        if row:
            return Task(task_id=row[0], title=row[1], desc=row[2])
        return None

    def list_all(self):
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        return [Task(task_id=row[0], title=row[1], desc=row[2]) for row in rows]

    def remove(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def clear(self) -> None:
        self.cursor.execute("DELETE FROM tasks")
        self.conn.commit()



