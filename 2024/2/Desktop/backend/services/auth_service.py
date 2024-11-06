from backend.database.crud import CRUD

class AuthService:
    def __init__(self, db_connection):
        self.crud = CRUD(db_connection)
        return 
    
    def authenticate_user(self, username, password):
        users = self.crud.read("usuarios", f"nomeUsuario = '{username}'")
        if users:
            user = users[0]
            if user["senhaUsuario"] == password:
                print("Authentication successful.")
                return user
            else:
                print("Invalid password.")
                return None
        else:
            print("User not found.")
            return None