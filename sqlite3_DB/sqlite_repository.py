import sqlite3


class TaskDB:
    def __init__(self,title,desc,id):
        self.title = title
        self.desc = desc
        self.id = id
        connector = sqlite3.connect('task_data_basa.db')
        cur = connector.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            title TEXT NOT NULL,
            description TEXT,
            id TEXT  PRIMARY KEY
        )
        """)
        connector.commit()
        connector.close()

    def write(self):
        connector = sqlite3.connect('task_data_basa.db')
        cur = connector.cursor()
        cur.execute(
            "INSERT INTO tasks (title,description,id) VALUES (?,?,?)",(self.title,self.desc,self.id)
        )
        connector.commit()
        connector.close()

    def remove(self):
        connector = sqlite3.connect('task_data_basa.db')
        cur = connector.cursor()
        cur.execute("DELETE FROM tasks WHERE id = ?",(self.id,))
        connector.commit()
        connector.close()

    def read_one(self):
        connector = sqlite3.connect('task_data_basa.db')
        cur = connector.cursor()
        cur.execute("SELECT * FROM tasks WHERE id = ?", (self.id,))
        row = cur.fetchone()
        connector.close()
        return row

    def read_all(self):
        connector = sqlite3.connect('task_data_basa.db')
        cur = connector.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        connector.close()
        return rows
    def update(self):
        pass




