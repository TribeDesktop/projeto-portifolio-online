import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matricula_backend import *
from messages_front import *

# Função para carregar imagens
def load_image(path, width, height):
    image = Image.open(path).convert("RGBA")
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Botão "Próximo"
def matricular_button_click():
    # Pega valores dos campos do formulário
    situacaoAluno = situacao_var.get()
    cursoID = curso_result.cget("text")
    cpfUsuario = cpf_result.cget("text")

    # Chama a função de cadastro do backend passando os dados vindos do formulário
    cadastrar = cadastrar_matricula(situacaoAluno, cursoID, cpfUsuario)
    if cadastrar == 'sucesso': 
        exibir_popup(Msg.title(1),(Msg.success("created","Matricula")))
        print("Mensagem de sucesso")
    else:
        exibir_popup("Erro!", ("Erro ao matricular o aluno"))
        print("Mensagem de erro")

# "Voltar"
def go_back():
    exit()

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

# Carregando imagem da seta
arrow_image = load_image("imgs/seta.png", 20, 15)

# Criar label e entrada de texto
def create_label_and_entry(text, row, column, colspan=1):
    label = tk.Label(content_frame, text=text, bg="white", font=("Montserrat Semibold", 10))
    label.grid(row=row, column=column, sticky="w", padx=20, pady=(10, 0))  # Ajusta o espaçamento
    entry = tk.Entry(content_frame, font=("Montserrat Semibold", 14), highlightbackground="lightgray", highlightcolor="lightgray", borderwidth=1, relief="solid")
    entry.grid(row=row + 1, column=column, columnspan=colspan, padx=20, pady=(0, 10), sticky="ew")
    content_frame.columnconfigure(column, weight=0)
    return entry

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

# Alterando a criação do OptionMenu
def create_optionmenu(text, row, column, colspan, options, default_value, callback):
    label = tk.Label(content_frame, text=text, bg="white", font=("Montserrat Semibold", 10))
    label.grid(row=row, column=column, columnspan=colspan, sticky="w", padx=20, pady=(10, 0))

    # Variável associada ao OptionMenu
    var = tk.StringVar()
    var.set(default_value)  # Define valor padrão
    
    # Criação do OptionMenu com a seta personalizada
    optionmenu = tk.OptionMenu(content_frame, var, *options, command=callback)
    optionmenu.config(font=("Montserrat Semibold", 13), highlightthickness=0, relief="solid", borderwidth=1, indicatoron=False, 
                      image=arrow_image, compound='right', bg="white")

    # Ajustar a largura do OptionMenu
    optionmenu.grid(row=row + 1, column=column, columnspan=colspan, padx=(20, 20), pady=(0, 10), sticky="ew")
    
    return var

# Função para atualizar as labels após seleção do curso
def update_course_info(selected_course):
    # Chama a função buscar_curso para obter os dados do curso
    course_data = buscar_curso(selected_course)

    if course_data:
        # Atualiza os valores das labels com base nos dados do curso
        curso_result.config(text=course_data["id"])
        sigla_result.config(text=course_data["sigla"])
        duracao_result.config(text=course_data["duracao"])
        periodo_result.config(text=course_data["periodo"])
        graduacao_result.config(text=course_data["graduacao"])
    else:
        # Caso o valor "Selecionar curso" seja mantido, deixa as labels padrão
        curso_result.config(text="Selecionar curso")
        sigla_result.config(text="Selecionar curso")
        duracao_result.config(text="Selecionar curso")
        periodo_result.config(text="Selecionar curso")
        graduacao_result.config(text="Selecionar curso")


#Função retorna nome e cpf
def update_aluno_info(selected_student):
    # Dicionário fictício com informações de cursos
    student_data = buscar_cpf(selected_student)
    
    if student_data and "cpf" in student_data:
        cpf_result.config(text=student_data["cpf"])  # Atualiza o label com o CPF do aluno
    else:
        cpf_result.config(text="Selecionar usuário")

# Lista de alunos
alunos = buscar_alunos_cadastrados()
# Criação do menu suspenso para selecionar o aluno
aluno_menu = create_optionmenu("Nome do Usuário:", 5, 0, 1, alunos, "Selecionar usuário", update_aluno_info)

cpf_label = tk.Label(content_frame, text="CPF do Usuário", bg="white", font=("Montserrat Semibold", 10))
cpf_label.grid(row=5, column=1, sticky="w", padx=20, pady=(0, 0))
cpf_result = tk.Label(content_frame, text="Selecionar usuário", bg="white", font=("Montserrat Semibold", 16), width="18")
cpf_result.grid(row=6, column=1, sticky="w", padx=20, pady=(0, 0))

nome_entry = create_label_and_entry("Nome do Curso:", 7, 0, colspan=2)

# Cursos disponíveis para seleção
cursos = buscar_cursos_cadastrados()
# Menu de opções para selecionar o curso, usando a função create_optionmenu
curso_menu = create_optionmenu("Selecionar Curso", 7, 0, 2, cursos, "Selecionar curso", update_course_info)

# ID do Curso e Sigla do Curso serão apenas Labels
curso_id_label = tk.Label(content_frame, text="ID do Curso:", bg="white", font=("Montserrat Semibold", 10))
curso_id_label.grid(row=7, column=2, sticky="w", padx=20, pady=(0, 0))
curso_result = tk.Label(content_frame, text="Selecionar curso", bg="white", font=("Montserrat Semibold", 16))
curso_result.grid(row=8, column=2, sticky="w", padx=20, pady=(0, 0))

sigla_label = tk.Label(content_frame, text="Sigla do Curso:", bg="white", font=("Montserrat Semibold", 10))
sigla_label.grid(row=9, column=2, sticky="w", padx=20, pady=(0, 0))
sigla_result = tk.Label(content_frame, text="Selecionar curso", bg="white", font=("Montserrat Semibold", 16))
sigla_result.grid(row=10, column=2, sticky="w", padx=20, pady=(0, 0))

#Duração
duracao_label = tk.Label(content_frame, text="Duração do Curso:", bg="white", font=("Montserrat Semibold", 10))
duracao_label.grid(row=9, column=0, sticky="w", padx=20, pady=(0, 0))
duracao_result = tk.Label(content_frame, text="Selecionar curso", bg="white", font=("Montserrat Semibold", 16))
duracao_result.grid(row=10, column=0, sticky="w", padx=20, pady=(0, 0))

#Período
periodo_label = tk.Label(content_frame, text="Período do Curso:", bg="white", font=("Montserrat Semibold", 10))
periodo_label.grid(row=11, column=2, sticky="w", padx=20, pady=(0, 0))
periodo_result = tk.Label(content_frame, text="Selecionar curso", bg="white", font=("Montserrat Semibold", 16))
periodo_result.grid(row=12, column=2, sticky="w", padx=20, pady=(0, 0))

#Tipo
graduacao_label = tk.Label(content_frame, text="Tipo de Graduação:", bg="white", font=("Montserrat Semibold", 10))
graduacao_label.grid(row=11, column=0, sticky="w", padx=20, pady=(0, 0))
graduacao_result = tk.Label(content_frame, text="Selecionar curso", bg="white", font=("Montserrat Semibold", 16))
graduacao_result.grid(row=12, column=0, sticky="w", padx=20, pady=(0, 0))

# Certifique-se de que as colunas têm pesos adequado
content_frame.columnconfigure(0, weight=1, minsize=230)  # Aumentando a largura mínima
content_frame.columnconfigure(1, weight=1, minsize=230)
content_frame.columnconfigure(2, weight=1, minsize=280)

# Criando os campos de opção
situacao_var = create_label_and_optionmenu("Situação da Matrícula:", 5, 2, 2, ['Ativo', 'Inativo', 'Pendente'])

# Botões "Voltar" e "Próximo" (sem frame)
back_button = tk.Button(bg_canvas, text="Voltar", command=go_back, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12))
back_button.place(relx=0.30, rely=0.88, anchor=tk.CENTER)  # Posiciona o botão no canvas

next_button = tk.Button(bg_canvas, text="Salvar", command=matricular_button_click, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12))
next_button.place(relx=0.70, rely=0.88, anchor=tk.CENTER)  # Posiciona o botão no canvas

# Adicionando logo ao canvas
logo_image = load_image("imgs/logo.png", 170, 76)
bg_canvas.create_image(30, 40, image=logo_image, anchor='nw')

# Iniciando o loop
root.mainloop()
