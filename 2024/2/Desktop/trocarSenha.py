import tkinter as tk
from tkinter import *
from tkinter import messagebox

class TrocarSenha(tk.Toplevel):
    def __init__(self, aplicacao): # aplicacao é a classe Aplicacao
        super().__init__(aplicacao)
        self.title("Troca de Senha")
        self.geometry("1280x720")
        self.configure(bg="white")
        self.controller = aplicacao
        
        # Conteúdo do Frame 3
        # Carregando as imagens da pasta 
        self.img5 = PhotoImage(file="imgs/fundoRedefinicaoSenha.png")

        # Criando os Labels que irão conter uma imagem
        self.lbl_back_f3 = Label(self,image=self.img5,background="white")

        # Criando as Labels que serão exibidas na tela
        self.lbl_text1 = Label(self.lbl_back_f3,text="Redefinição de Senha:", background="#2792B2", foreground="white", font="Montserrat 34 bold")
        self.lbl_text2 = Label(self.lbl_back_f3,text="Senha atual:", background="#2985AF", foreground="white", font="Montserrat 15 bold")
        self.txt_textBox1 = Entry(self.lbl_back_f3,font="Montserrat 15")
        self.lbl_text3 = Label(self.lbl_back_f3,text="Digite a nova Senha:", background="#2B6CA6", foreground="white", font="Montserrat 15 bold")
        self.txt_textBox2 = Entry(self.lbl_back_f3,font="Montserrat 15")
        self.lbl_text4 = Label(self.lbl_back_f3,text="Confirme a Senha:", background="#2E539F", foreground="white", font="Montserrat 15 bold")
        self.txt_textBox3 = Entry(self.lbl_back_f3,font="Montserrat 15")
        self.btn_conf = Button(self.lbl_back_f3,text="Confirmar", font="Montserrat 15 bold", foreground="#331C8F", command=self.atualizarSenha)

        # Salvando e posicionado os labes dentro do Frame
        self.lbl_back_f3.pack()
        self.lbl_text1.place(x=130,y=90)
        self.lbl_text2.place(x=130,y=170)
        self.txt_textBox1.place(x=135,y=215,width=555,height=50)
        self.lbl_text3.place(x=130,y=290)
        self.txt_textBox2.place(x=135,y=335,width=555,height=50)
        self.lbl_text4.place(x=130,y=410)
        self.txt_textBox3.place(x=135,y=455,width=555,height=50)
        self.btn_conf.place(x=130,y=580,width=565,height=50)

    def atualizarSenha(self):
        senha_atual = self.txt_textBox1.get()
    
        nova_senha = self.txt_textBox2.get()
        confirmar_nova_senha = self.txt_textBox3.get()
    
        usuario = self.controller.user_session.current_user # pegar os dados do usuário logado.
        
        if senha_atual == usuario["senhaUsuario"]: # verifica se a senha atual é igual à senha no banco de dados
            if nova_senha == confirmar_nova_senha:
                
                update_senha = { "senhaUsuario": nova_senha } # atualizar o campo senhaUsuario do banco de dados com a nova senha fornecida
                self.controller.app_service.update_user(usuario["usuarioID"], update_senha)
        
                messagebox.showinfo("Info", f"Senha atualizada para o usuário {usuario["nomeUsuario"]}")
                self.controller.criar_menu()
                self.destroy()
            else:
                messagebox.showinfo("Info", f"Senhas devem ser iguais!")
        else:
            messagebox.showinfo("Info", f"Senha atual está errada!") 

#    def alterar(self):
    #   messagebox.showinfo("","Senha Alterada com Sucesso!")
#        self.destroy()