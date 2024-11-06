## **__exemplo de uso: __**


### **Usando funções da classe Crud  (./database)**
```python
######################
#### TESTING CRUD ####
######################

from database.db_connection import DBConnection
from database.crud          import CRUD

config = {
  "user"             : "root",
  "password"         : "",
  "host"             : "127.0.0.1",
  "database"         : "escola",
  "raise_on_warnings": True
}

db = DBConnection(config)
db.connect()
app = CRUD(db)

dataAdmin = {
    "usuarioAdmin": "ademir",
    "emailAdmin"  : "ademir@gmail.com" 
}
# app.create("secretarias", dataAdmin)

dataUser = {
    "nomeUsuario"      : "gabriell",
    "senhaUsuario"     : "123123",
    "dataNascUsuario"  : "2004-06-21",
    "sexoUsuario"      : "m",
    "cpfUsuario"       : "111111111-11",
    "tipoUsuario"      : "aluno",
    "ativo"            : 1,
    "adminID"          : 1,
}
# app.create("usuarios", dataUser)
# last_address_id = app.cursor.lastrowid

users = app.read("usuarios", f"nomeUsuario = 'gabriell'")

if users:
  user = users[0]
  print(user['nomeUsuario'])
  print(user)
```

### **Usando funções das classe AppService e Session (./services)**
```python
########################################
#### TESTING AUTHENTICATION SERVICE ####
########################################

from database.db_connection import DBConnection
from services.app_service   import AppService
from services.session       import Session

config = {
  "user"             : "root",
  "password"         : "",
  "host"             : "127.0.0.1",
  "database"         : "escola",
  "raise_on_warnings": True
}

db = DBConnection(config)
db.connect()

app_service = AppService(db)
app_service.login("gabriell", "123123")

# verifying if user is logged:
if Session.is_logged_in():
    print(f"Bem-vindo, {Session.current_user['nomeUsuario']}!")
else:
    print("Por favor, faça login.")



# getting data of the logged user
if Session.is_logged_in():
    user_id = Session.current_user["usuarioID"]
    user_data = app_service.get_user_data(user_id)
    print(user_id)
    print(user_data)

db.disconnect()
```