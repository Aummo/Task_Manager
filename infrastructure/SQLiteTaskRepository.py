
import sqlite3
from typing import Optional

from ..repositories.task_repository import TaskRepository
from ..domain.task import Task

class SQLiteTaskRepository(TaskRepository):

    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("\n"
                            "            CREATE TABLE IF NOT EXISTS tasks (\n"
                            "                id TEXT PRIMARY KEY,\n"
                            "                title TEXT NOT NULL,\n"  
                            "                description TEXT,\n"
                            "                user_id TEXT NOT NULL\n"
                            "            )\n"
                            "        ")
        self.conn.commit()

    def add(self, task):
        self.cursor.execute(
            "INSERT INTO tasks (id, title, description, user_id) VALUES (?, ?, ?, ?)",
            (task.id, task.title, task.desc, task.user_id)
        )
        self.conn.commit()

    def get_by_id(self, task_id: str) -> Optional[Task]:
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()
        if row:
            return Task(task_id=row[0], title=row[1], desc=row[2], user_id=row[3])
        return None

    def list_all(self):
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        return [Task(task_id=row[0], title=row[1], desc=row[2], user_id=row[3]) for row in rows]

    def remove(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def clear(self) -> None:
        self.cursor.execute("DELETE FROM tasks")
        self.conn.commit()



