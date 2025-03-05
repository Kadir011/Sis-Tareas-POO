import os
import json 
from typing import List, Dict
from classes.task import Task
from classes.user import User

class FileRepository:
    def __init__(self, tasks_file: str = "json/tasks.json", users_file: str = "json/users.json"):
        self.tasks_file = tasks_file
        self.users_file = users_file

    def save_tasks(self, tasks: List[Task]) -> None:
        with open(self.tasks_file, 'w', encoding='utf-8') as file:
            data = {task.name: task.status for task in tasks}
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_tasks(self) -> List[Task]:
        if not os.path.exists(self.tasks_file):
            return []
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Task(name, status) for name, status in data.items()]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_users(self, users: Dict[str, User]) -> None:
        with open(self.users_file, 'w', encoding='utf-8') as file:
            json.dump({
                username: user.__dict__
                for username, user in users.items()
            }, file, ensure_ascii=False, indent=4)

    def load_users(self) -> Dict[str, User]:
        if not os.path.exists(self.users_file):
            return {}
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return {
                    username: User(**user_data)
                    for username, user_data in data.items()
                }
        except (json.JSONDecodeError, FileNotFoundError):
            return {}




