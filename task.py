class Task:
    def __init__(self, title='', desc='', id=None):  
        self.id = id
        self.title = title
        self.desc = desc
    
    def __str__(self):
        return f"{self.id}. {self.title} - {self.desc}"
