class Task:
    def __init__(self,task_id:str,title:str,user_id:str,desc:str=''):

        if  not title or not title.strip():
            raise ValueError('Task title cannot be empty')
        self._id = task_id
        self._title = title
        self._desc = desc
        self._user_id = user_id
    @property
    def id(self):
        return self._id
    @property
    def title(self):
        return self._title
    @property
    def desc(self):
        return self._desc
    @property
    def user_id(self):
        return self._user_id


    def rename(self,new_title:str):
        if not new_title or not new_title.strip():
            raise ValueError('Task title cannot be empty')
        self._title = new_title

    def change_desc(self,new_desc):
        self._desc = new_desc or ''

    def summary(self) -> str:
        return f'{self._id},{self._title} - {self._desc}'
