from datetime import datetime

class TodoTask:
    def __init__(self, id=None, title="", description="", deadline=None, priority="中", completed=False):
        self.id = id  # データベースID (Noneは新規作成時)
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = completed