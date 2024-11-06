import tkinter as tk
from tkinter import *
from tkinter import messagebox, PhotoImage, Image, font

from backend.database.db_connection import DBConnection
from backend.services.app_service   import AppService
from backend.services.session       import Session

import usuario
import trocarSenha
import login

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.firstTime = 0
        login.Login(self)
        self.withdraw()
        
        config = {
            "user"             : "root",
            "password"         : "",
            "host"             : "127.0.0.1",
            "database"         : "escola",
            "raise_on_warnings": True
        }
        
        db = DBConnection(config)
        db.connect()
        
        self.app_service = AppService(db)
        
        self.user_session = Session()


### CHAMADAS DO MENU ###
    def cadastros(self):
        Cadastro(self)

    def senhas(self):
        Senhas(self)

    def emConstrucao(self):
        messagebox.showinfo("Atenção", "Funcionalidade em Construção")


### MENU ###
    def criar_menu(self):
        # Carregando imagem da pasta
        self.title("Menu Principal")
        self.deiconify()
        self.geometry("1280x720")
        self.resizable(False,False)
        self.img4 = PhotoImage(file="imgs/tela_opcoes.png")
        self.label1 = Label(self, image=self.img4, bg="#26A7B9")
        self.label1.place(x=0, y=0)
        
        # Botões
        self.custom_font = font.Font(family="Helvetica", size=15, weight="bold")
        self.btn_matricula = Button(self.label1, text="Matrícula", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=10, height=1, command=self.emConstrucao)
        self.btn_matricula.place(x=170, y=10)

        self.btn_notas = Button(self.label1, text="Notas", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=8, height=1, command=self.emConstrucao)
        self.btn_notas.place(x=320, y=10)

        self.btn_boletim = Button(self.label1, text="Boletim", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=9, height=1, command=self.emConstrucao)
        self.btn_boletim.place(x=470, y=10)

        self.btn_trocar_senha = Button(self.label1, text="Cadastro", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.cadastros)
        self.btn_trocar_senha.place(x=620, y=10)

        self.btn_trocar_senha = Button(self.label1, text="Senhas", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.senhas)
        self.btn_trocar_senha.place(x=815, y=10)

        self.btn_sair = Button(self.label1, text="Sair", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=8, height=1, command=self.quit)
        self.btn_sair.place(x=1000, y=10)
            
### CADASTROS ###
class Cadastro(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro")
        self.geometry("150x247+700+90")
        self.overrideredirect(True)
        self.resizable(False, False)
        self.controller = master # self.controller é a classe Aplicacao
        
        self.custom_font = font.Font(family="Helvetica", size=15, weight="bold")
        self.btn_usuarios = Button(self, text="Usuarios", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.cadastroUsuario)
        self.btn_usuarios.place(x=0, y=0)

        self.btn_cursos = Button(self, text="Cursos", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.emConstrucao)
        self.btn_cursos.place(x=0, y=30)

        self.btn_turmas = Button(self, text="Turmas", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.emConstrucao)
        self.btn_turmas.place(x=0, y=60)

        self.btn_disciplinas = Button(self, text="Disciplinas", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.emConstrucao)
        self.btn_disciplinas.place(x=0, y=90)

        self.btn_disciplinas = Button(self, text="Horários", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.emConstrucao)
        self.btn_disciplinas.place(x=0, y=120)

        self.btn_disciplinas = Button(self, text="Atividades", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.emConstrucao)
        self.btn_disciplinas.place(x=0, y=150)

        self.btn_disciplinas = Button(self, text="Disa Letivos", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.emConstrucao)
        self.btn_disciplinas.place(x=0, y=180)

        self.btn_disciplinas = Button(self, text="Secretarias", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.emConstrucao)
        self.btn_disciplinas.place(x=0, y=210)

    def cadastroUsuario(self):
        usuario.Usuario(self.controller) # enviar a classe Aplicacao para a classe Usuario
        self.controller.withdraw()
        self.withdraw()
        

    def emConstrucao(self):
        messagebox.showinfo("Atenção", "Funcionalidade em Construção")
        self.destroy()

### SENHAS ###
class Senhas(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Senhas")
        self.geometry("150x67+900+90")
        self.overrideredirect(True)
        self.resizable(False, False)
        self.controller = master
        
        self.custom_font = font.Font(family="Helvetica", size=15, weight="bold")
        self.btn_usuarios = Button(self, text="Trocar Senha", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.trocarSenha)
        self.btn_usuarios.place(x=0, y=0)

        self.btn_cursos = Button(self, text="Novo Login", font=self.custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=self.login)
        self.btn_cursos.place(x=0, y=30)

    def trocarSenha(self):
        trocarSenha.TrocarSenha(self.controller)
        self.controller.withdraw()
        self.withdraw()
         
    def login(self):
        login.Login(self.controller)
        self.controller.withdraw()
        self.withdraw()
    
### EXECUÇÂO ###
if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
