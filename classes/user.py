from dataclasses import dataclass
import random, string 

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    username: str
    password: str

    @staticmethod
    def generate_random_password(length: int = 12) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
    



