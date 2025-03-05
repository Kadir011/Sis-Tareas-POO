from dataclasses import dataclass 

@dataclass
class Task:
    name: str
    status: bool = False

    def mark_as_done(self) -> None:
        self.status = True

    def __str__(self) -> str:
        return f"{self.name} - {'Terminado' if self.status else 'Pendiente'}"







