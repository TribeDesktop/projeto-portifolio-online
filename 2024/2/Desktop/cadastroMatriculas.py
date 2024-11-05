import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Função para carregar imagens
def load_image(path, width, height):
    image = Image.open(path).convert("RGBA")
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Botão "Próximo"
def next_page():
    print("Próxima página")

# "Voltar"
def go_back():
    print("Página anterior")

# Criação da janela principal
root = tk.Tk()
root.title("Matrícula de Aluno")

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
background_image = load_image("imgs/lado_direito.png", int(window_width * 0.75), int(window_height * 0.71))
bg_canvas.create_image(window_width//2, window_height//2, image=background_image, anchor=tk.CENTER)

# Frame para os campos de entrada (com tamanho fixo)
content_frame = tk.Frame(bg_canvas, bg="white") 
content_frame.place(relx=0.51, rely=0.52, anchor=tk.CENTER, width=window_width/1.55, height=window_height/1.67)

# Título
title_label = tk.Label(content_frame, text="Matrícula de Aluno", font=("Montserrat Bold", 18), bg="white", fg="#004080")
title_label.grid(row=0, column=0, columnspan=3, pady=1, sticky="w", padx=15)

# Subtítulo
subtitle_label = tk.Label(content_frame, text="Insira as informações para concluir a matrícula:", font=("Montserrat Semibold", 11), bg="white", fg="black", width=40)
subtitle_label.grid(row=1, column=0, columnspan=2, pady=0, sticky="w", padx=0)

# Criar label e entrada de texto
def create_label_and_entry(text, row, column, colspan=1):
    label = tk.Label(content_frame, text=text, bg="white", font=("Montserrat Semibold", 10))
    label.grid(row=row, column=column, sticky="w", padx=20, pady=(10, 0))  # Ajusta o espaçamento
    entry = tk.Entry(content_frame, font=("Montserrat Semibold", 14), highlightbackground="lightgray", highlightcolor="lightgray", borderwidth=1, relief="solid")
    entry.grid(row=row + 1, column=column, columnspan=colspan, padx=20, pady=(0, 10), sticky="ew")
    content_frame.columnconfigure(column, weight=0)
    return entry


# Criando os campos de entrada
sigla_entry = create_label_and_entry("ID da Matrícula:", 5, 0)
sigla_entry = create_label_and_entry("ID do Usuário:", 5, 1)
nome_entry = create_label_and_entry("ID do Curso:", 5, 2)
nome_entry = create_label_and_entry("Nome do Curso:", 7, 0, colspan=2)
nome_entry = create_label_and_entry("Situação da Matrícula:", 7, 2)
nome_entry = create_label_and_entry("Sigla do Curso:", 9, 2, colspan=2)

# Carregando imagem da seta
arrow_image = load_image("imgs/seta.png", 20, 15)

# Alterando a criação do OptionMenu
def create_label_and_optionmenu(text, row, column, colspan, options):
    label = tk.Label(content_frame, text=text, bg="white", font=("Montserrat Semibold", 10))
    label.grid(row=row, column=column, columnspan=colspan, sticky="w", padx=20, pady=(10, 0))

    # Variável associada ao OptionMenu
    var = tk.StringVar()
    var.set(options[0])  # Define valor padrão
    
    # Criação do OptionMenu com a seta personalizada
    optionmenu = tk.OptionMenu(content_frame, var, *options)
    optionmenu.config(font=("Montserrat Semibold", 13), highlightthickness=0, relief="solid", borderwidth=1, indicatoron=False, 
                      image=arrow_image, compound='right', bg="white")

    # Ajustar a largura do OptionMenu
    optionmenu.grid(row=row + 1, column=column, columnspan=2, padx=(20, 20), pady=(0, 10), sticky="ew")
    
    # Ajuste de largura mínima

    return var

# Certifique-se de que as colunas têm pesos adequado
content_frame.columnconfigure(0, weight=1, minsize=230)  # Aumentando a largura mínima
content_frame.columnconfigure(1, weight=1, minsize=230)
content_frame.columnconfigure(2, weight=1, minsize=280)


# Criando os campos de opção
tipo_duracao_var = create_label_and_optionmenu("Duração:", 9, 0, 2, ["Anual", "Semestral"])
periodo_curso_var = create_label_and_optionmenu("Período:", 11, 2, 1, ["Matutino", "Vespertino", "Noturno"])
tipo_graduacao_var = create_label_and_optionmenu("Tipo de Graduação:", 11, 0, 1, ['Bacharelado','Licenciatura','Tecnólogo','Mestrado','Doutorado'])


# Botões "Voltar" e "Próximo" (sem frame)
back_button = tk.Button(bg_canvas, text="Voltar", command=go_back, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12))
back_button.place(relx=0.30, rely=0.88, anchor=tk.CENTER)  # Posiciona o botão no canvas

next_button = tk.Button(bg_canvas, text="Próximo", command=next_page, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12))
next_button.place(relx=0.70, rely=0.88, anchor=tk.CENTER)  # Posiciona o botão no canvas

# Adicionando logo ao canvas
logo_image = load_image("imgs/logo.png", 170, 76)
bg_canvas.create_image(30, 40, image=logo_image, anchor='nw')

# Iniciando o loop
root.mainloop()