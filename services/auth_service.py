from data.storage import FileRepository 
from classes.user import User
from typing import Optional, Dict , List

class AuthService:
    def __init__(self, repository: FileRepository):
        self.repository = repository
        self.users = repository.load_users() 
    
    def register(self) -> User:
        first_name = input("Ingresar nombre: ")
        last_name = input("Ingresar apellido: ")
        email = input("Ingresar email: ")
        username = input("Ingresar usuario: ") 

        if username in self.users:
            raise ValueError('El usuario ya existe.') 
        
        random_pass = input("Generar contraseña aleatoria (si/no): ").lower() == 'si'
        password = User.generate_random_password() if random_pass else input("Ingresar contraseña: ") 

        user = User(first_name, last_name, email, username, password)
        self.users[username] = user
        self.repository.save_users(self.users) 
        print(f'Usuario registrado con éxito. Contraseña: {password}') 
        return user 
    
    def login(self) -> Optional[User]:
        username = input("Ingresar usuario: ")
        password = input("Ingresar contraseña: ") 

        user = self.users.get(username)
        if user and user.password == password: 
           return user 
        print('Credenciales incorrectas. Intente nuevamente.')
        return None 
    
    def change_password(self, username:str) -> bool:
        if username not in self.users:
           return False 
        
        random_pass = input("Generar contraseña aleatoria (si/no): ").lower() == 'si'
        new_password = User.generate_random_password() if random_pass else input("Ingresar nueva contraseña: ")
        self.users[username].password = new_password
        self.repository.save_users(self.users)
        print(f'Contraseña cambiada con éxito. Nueva contraseña: {new_password}')
        return True 


