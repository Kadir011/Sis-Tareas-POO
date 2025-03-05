from typing import List, Optional
from classes.task import Task
from data.storage import FileRepository

class TaskService:
    def __init__(self, repository: FileRepository):
        self.repository = repository
        self.tasks = repository.load_tasks()

    def add_tasks(self, num_tasks: int) -> None:
        for i in range(num_tasks):
            task_name = input(f"Ingresar tarea {i+1}: ") 
            self.tasks.append(Task(task_name))
        self.repository.save_tasks(self.tasks)

    def get_task_by_index(self, index: int) -> Optional[Task]:
        return self.tasks[index] if 0 <= index < len(self.tasks) else None

    def search_tasks(self, query: str) -> List[Task]:
        if query.isdigit():
            index = int(query) - 1
            task = self.get_task_by_index(index)
            return [task] if task else []
        return [task for task in self.tasks if query.lower() in task.name.lower()]

    def update_task(self, index: int, new_name: str) -> bool:
        if task := self.get_task_by_index(index):
            task.name = new_name
            self.repository.save_tasks(self.tasks)
            return True
        return False

    def delete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.repository.save_tasks(self.tasks)
            return True
        return False

    def mark_task_as_done(self, index: int) -> bool:
        if task := self.get_task_by_index(index):
            task.mark_as_done()
            self.repository.save_tasks(self.tasks)
            return True
        return False

    def get_all_tasks(self) -> List[Task]:
        return self.tasks 

