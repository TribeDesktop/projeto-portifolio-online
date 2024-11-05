import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from curso_backend import cadastrar_curso
from messages_front import *

#Função para carregar imagens
def load_image(path, width, height):
    image = Image.open(path).convert("RGBA")
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Botão "Próximo"
def cadastrar_button_click():
    # Pega valores dos campos do formulário
    nome = nome_entry.get()
    sigla = sigla_entry.get()
    tipo_duracao = tipo_duracao_var.get()
    periodo_curso = periodo_curso_var.get()
    tipo_graduacao = tipo_graduacao_var.get()

    # Chama a função de cadastro do backend passando os dados vindos do formulário
    cadastrar = cadastrar_curso(nome, sigla, tipo_duracao, periodo_curso, tipo_graduacao)
    if cadastrar == 'sucesso': 
        exibir_popup(Msg.title(1),(Msg.success("created","Curso")))
    else:
        exibir_popup("Erro!", ("Erro ao cadastrar o curso"))
    
# "Voltar"
def go_back():
    exit()

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Curso")

# Obtém a largura e altura da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define a largura e altura da janela como 100% da tela
window_width = int(screen_width * 1)
window_height = int(screen_height * 1)

# Define a geometria da janela
# root.geometry(f"{window_width}x{window_height}")
root.geometry(f"1920x1080")

# Bloquear redimensionamento
root.resizable(False, False)

# Centraliza a janela na tela
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Criação do canvas para o fundo
bg_canvas = tk.Canvas(root, width=window_width, height=window_height)
bg_canvas.place(x=0, y=0)

# Desenha o fundo azul claro
for i in range(window_width):
    color = f'#{int(39 + (51 - 39) * (i / window_width)):02X}{int(167 + (28 - 167) * (i / window_width)):02X}{int(185 + (143 - 185) * (i / window_width)):02X}'
    bg_canvas.create_line(i, 0, i, window_height, fill=color)

# Carregar imagem de fundo
background_image = load_image("imgs/lado_direito.png", int(window_width * 0.60), int(window_height * 0.65))
bg_canvas.create_image(window_width//2, window_height//2, image=background_image, anchor=tk.CENTER)

# Frame para os campos de entrada (com tamanho fixo)
content_frame = tk.Frame(bg_canvas, bg="white", width=300, height=500) 
content_frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER, width=window_width/2, height=window_height/2.1)

# Título
title_label = tk.Label(content_frame, text="Cadastro de Curso", font=("Montserrat Bold", 20), bg="white", fg="#004080")
title_label.grid(row=0, column=0, columnspan=2, pady=1, sticky="w", padx=15)

# Subtítulo
subtitle_label = tk.Label(content_frame, text="Insira as informações para concluir o cadastro:", font=("Montserrat Semibold", 12), bg="white", fg="black")
subtitle_label.grid(row=1, column=0, columnspan=2, pady=0, sticky="w", padx=15)

# Criar label e entrada de texto
def create_label_and_entry(text, row, column, colspan=1):
    label = tk.Label(content_frame, text=text, bg="white", font=("Montserrat Semibold", 10))
    label.grid(row=row, column=column, sticky="w", padx=20, pady=(10, 0))  # Ajusta o espaçamento
    entry = tk.Entry(content_frame, font=("Montserrat Semibold", 14), highlightbackground="lightgray", highlightcolor="lightgray", borderwidth=1, relief="solid")
    entry.grid(row=row + 1, column=column, columnspan=colspan, padx=20, pady=(0, 10), sticky="ew")
    content_frame.columnconfigure(column, weight=0)
    return entry


# Criando os campos de entrada
nome_entry = create_label_and_entry("Nome do curso:", 4, 0, colspan=2)
sigla_entry = create_label_and_entry("Sigla do curso:", 6, 0)

# Carregando imagem da seta
arrow_image = load_image("imgs/seta.png", 20, 15)

# Campos de opção (OptionMenu) com seta personalizada
def create_label_and_optionmenu(text, row, column, options):
    label = tk.Label(content_frame, text=text, bg="white", font=("Montserrat Semibold", 10))
    label.grid(row=row, column=column, sticky="w", padx=20, pady=(10, 0))

    # Variável associada ao OptionMenu
    var = tk.StringVar()
    var.set(options[0])  # Definir valor padrão
    
    # Criação do OptionMenu com a seta personalizada
    optionmenu = tk.OptionMenu(content_frame, var, *options)
    optionmenu.config(font=("Montserrat Semibold", 13), highlightthickness=0, relief="solid", borderwidth=1, indicatoron=False, 
                      image=arrow_image, compound='right', bg="white")

    # Ajuste do padding para garantir equilíbrio
    optionmenu.grid(row=row + 1, column=column, padx=(20, 20), pady=(0, 10), sticky="ew")
    return var

# Configuração de pesos e tamanhos mínimos para colunas
content_frame.columnconfigure(0, weight=1, minsize=200)
content_frame.columnconfigure(1, weight=1, minsize=200)

# Criando os campos de opção
tipo_duracao_var = create_label_and_optionmenu("Tipo de duração:", 6, 1, ["Anual", "Semestral"])
periodo_curso_var = create_label_and_optionmenu("Período do curso:", 8, 0, ["Matutino", "Vespertino", "Noturno"])
tipo_graduacao_var = create_label_and_optionmenu("Tipo de graduação do curso:", 8, 1, ['Bacharelado','Licenciatura','Tecnólogo','Mestrado','Doutorado'])


# Botões "Voltar" e "Próximo" (sem frame)
back_button = tk.Button(bg_canvas, text="Voltar", command=go_back, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12))
back_button.place(relx=0.40, rely=0.85, anchor=tk.CENTER)  # Posiciona o botão no canvas

next_button = tk.Button(bg_canvas, text="Cadastrar", command=cadastrar_button_click, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12))
next_button.place(relx=0.60, rely=0.85, anchor=tk.CENTER)  # Posiciona o botão no canvas

# Adicionando logo ao canvas
logo_image = load_image("imgs/logo.png", 180, 80)
bg_canvas.create_image(30, 40, image=logo_image, anchor='nw')

# Iniciando o loop
root.mainloop()
