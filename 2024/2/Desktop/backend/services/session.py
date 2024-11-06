# TODO:
# make the session persistent

class Session:
    current_user = None # Após login, a função AppService.login() irá preencher a variável current_user com os dados do usuário logado.

    @classmethod
    def is_logged_in(cls):
        return cls.current_user is not None

    # As funções abaixo são funções auxiliares para AppService, você NÃO deve usá-los!

    @classmethod
    def login(cls, user_data):
        cls.current_user = user_data
        print(f"Usuário {user_data['nomeUsuario']} logado.")

    @classmethod
    def logout(cls):
        print(f"Usuário {cls.current_user['nomeUsuario']} deslogado.")
        cls.current_user = None