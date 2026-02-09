class Task:
    def __init__(self,tas_id:str,title:str,desc:str=''):

        if  not title or not title.strip():
            raise ValueError('Task title cannot be empty')
        self._id = tas_id
        self._title = title
        self._desc = desc

    @property
    def id(self):
        return self._id

    def rename(self,new_title:str):
        if new_title or not new_title.strip():
            raise ValueError('Task title cannot be empty')
        self._title = new_title

    def change_desc(self,new_desc):
        self._desc = new_desc or ''

    def summary(self) -> str:
        return f'{self._id},{self._title} - {self._desc}'

