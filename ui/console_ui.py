import time
from services.task_service import TaskService
from services.auth_service import AuthService
from data.storage import FileRepository 

class ConsoleUI:
    def __init__(self):
        self.repository = FileRepository()
        self.auth_service = AuthService(self.repository)
        self.current_user = None 
    
    def get_user_input(self, prompt: str) -> str:
        return input(prompt).strip()
    
    def show_auth_menu(self):
        while not self.current_user:
            print('=== Bienvenido ===')
            print('1. Iniciar sesión')
            print('2. Registrarse')
            print('3. Salir') 

            try:
                option = int(self.get_user_input('Opción: '))
                match option:
                    case 1:
                        self.current_user = self.auth_service.login()
                    case 2:
                        self.current_user = self.auth_service.register()
                    case 3:
                        print('Adiós!')
                        break
                    case _:
                        print('Opción inválida') 
            except ValueError:
                print('Opción inválida')
    
    def show_task_menu(self):
        task_service = TaskService(self.repository) 

        while True:
            print(f'\n=== Bienvenido {self.current_user.username} ===') 
            print('1. Mostrar tareas')
            print('2. Añadir tarea')
            print('3. Buscar tarea')
            print('4. Actualizar tarea')
            print('5. Eliminar tarea')
            print('6. Marcar tarea como terminada')
            print('7. Cambiar contraseña')
            print('8. Salir') 

            try:
                option = int(self.get_user_input('\nOpción: '))
                match option:
                    case 1:
                        tasks = task_service.get_all_tasks() 
                        if not tasks:
                            print('No hay tareas registradas.')
                        
                        for i, task in enumerate(tasks, 1):
                            print(f'{i}. {task}') 
                    case 2:
                        num_tasks = int(self.get_user_input('Ingresar número de tareas: ')) 
                        if num_tasks < 0:
                            print('El número de tareas debe ser positivo.')
                            return
                        
                        task_service.add_tasks(num_tasks)
                        print(f'{num_tasks} tareas añadidas con éxito.')
                    case 3:
                        query = self.get_user_input('Ingresar palabra clave o índice: ') 
                        results = task_service.search_tasks(query)
                        if not results:
                            print('No hay resultados.')
                        
                        print('Se encontró:', ', '.join(str(task) for task in results)) 
                    case 4:
                        index = int(self.get_user_input('Índice: ')) - 1 
                        new_name = self.get_user_input('Nueva tarea: ')
                        if not task_service.update_task(index, new_name):
                            print('Índice inválido.') 
                        
                        print('Tarea actualizada con éxito.') 
                    case 5:
                        index = int(self.get_user_input('Índice: ')) - 1
                        if not task_service.delete_task(index):
                            print('Índice inválido.')
                        
                        print('Tarea eliminada con éxito.') 
                    case 6:
                        index = int(self.get_user_input('Índice: ')) - 1
                        if not task_service.mark_task_as_done(index):
                            print('Índice inválido.')
                        
                        print('Tarea marcada como terminada con éxito.')
                    case 7:
                        if self.auth_service.change_password(self.current_user.username):
                            print('Por favor, inicie sesión nuevamente.') 
                            self.current_user = None
                            return
                    case 8:
                        print(f'Adiós {self.current_user.username}!')
                        exit()
                    case _:
                        print('Opción inválida. Intente nuevamente.')
                        time.sleep(5)
            except ValueError:
                print('Opción inválida')
    
    def run(self):
        while True:
            if not self.current_user:
                self.show_auth_menu()
            else:
                self.show_task_menu()





