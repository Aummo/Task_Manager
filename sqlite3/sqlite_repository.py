import sqlite3


class sqlite:
    def __init__(self,title,desc,id):
        self.title = title
        self.desc = desc
        self.id = id
        connector = sqlite3.connect('task_data_basa.db')
        cur = connector.cursor()

        cur.execute("""""
        CREATE TABLE IF NOT EXISTS task (
            title TEXT NOT NULL,
            description TEXT,
            id TEXT NOT NULL
        )
        """"")
        connector.commit()

    def write(self):
        pass

    def read(self):
        pass

    def update(self):
        pass




