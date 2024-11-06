from backend.database.crud         import CRUD
from backend.services.auth_service import AuthService
from backend.services.session      import Session

# TODO: 
# token
# implement fuctions to register new users
# persistent login

class AppService:
    def __init__(self, db_connection):
        self.crud = CRUD(db_connection)
        self.auth_service = AuthService(db_connection)

    def get_initial_view(self):
        user_count = self.crud.read("usuarios", condition="1")
        if not user_count:
            return "register"
        else:
            return "login"

    def get_user_data(self, user_id): # retorna dados de um usuário. Para usuários logados use current_user em session.py
        user_data = self.crud.read("usuarios", f"usuarioID= {user_id}")
        return user_data[0]

    def update_user(self, user_id, updates): # Atualiza campos do usuário conforme o dicionário recebido.
        self.crud.update("usuarios", updates, f"usuarioID= {user_id}")
        return 

    def login(self, username, password):
        user = self.auth_service.authenticate_user(username, password)
        if user:
            Session.login(user)
            return True
        return False

    def logout(self):
        if Session.is_logged_in():
            Session.logout()
            return True
        return False
    
    # def register_user(self, user_data):
    #     if not self.auth_service.validate_user_data(user_data):
    #         return False

    #     self.crud.create("usuarios", user_data)

    #     token = self.auth_service.generate_token(user_data)
    #     return token