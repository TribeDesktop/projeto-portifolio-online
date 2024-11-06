import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from turma_backend import *
from messages_front import *

def cadastrar_button_click():
    # Pega valores dos campos do formulário
    nome = nome_entry.get()
    sigla = sigla_entry.get()
    data_inicio = data_inicio_entry.get()
    data_fim = data_fim_entry.get()

    # Coleta os dias não letivos e descrições
    dias_nao_letivos_input = dias_nao_letivos_entry.get().strip()  # Coletando do campo Text
    descricao_dia_nao_letivo_input = descricao_dia_entry.get("1.0", tk.END).strip()  # Coletando do campo Text

    try:
        # Chama a função de backend para processar os dias e descrições
        dias_nao_letivos = processar_dias_nao_letivos(dias_nao_letivos_input, descricao_dia_nao_letivo_input)
        print(dias_nao_letivos)
    except ValueError as e:
        print(f"Erro: {str(e)}")
        return  # Sai da função sem cadastrar
    
    # Chama a função para realizar o cadastro
    cadastrar_turma(nome, sigla, data_inicio, data_fim, dias_nao_letivos)
    exibir_popup(Msg.title(1),(Msg.success("created","Turma")))
    
def load_image(path, width, height):
    image = Image.open(path).convert("RGBA")
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

def next_page():
    print("Próxima página")

def go_back():
    print("Página anterior")

    
root = tk.Tk()
root.title("Cadastro da Turma")

root.geometry(f"1280x720")
root.resizable(False, False)

bg_canvas = tk.Canvas(root, width=1280, height=720)
bg_canvas.place(x=0, y=0)

for i in range(1280):
    color = f'#{int(39 + (51 - 39) * (i / 1280)):02X}{int(167 + (28 - 167) * (i / 1280)):02X}{int(185 + (143 - 185) * (i / 1280)):02X}'
    bg_canvas.create_line(i, 0, i, 720, fill=color)
    
content_frame = tk.Frame(bg_canvas, bg="white", width=800, height=400) 
content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
content_frame.grid_propagate(False)
    
title_label = tk.Label(content_frame, text="Cadastro da Turma", font=("Montserrat Bold", 20), bg="white", fg="#004080")
title_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="w", padx=15)

subtitle_label = tk.Label(content_frame, text="Insira as informações para concluir o cadastro:", font=("Montserrat Semibold", 12), bg="white", fg="black")
subtitle_label.grid(row=1, column=0, columnspan=4, pady=0, sticky="w", padx=15)

def create_label_and_entry(text, row, column, colspan=1, width=20, widget_type='entry'):
    label = tk.Label(content_frame, text=text, bg="white", font=("Montserrat Semibold", 10))
    label.grid(row=row, column=column, sticky="w", padx=20, pady=(10, 0))
    
    if widget_type == 'entry':
        entry = tk.Entry(content_frame, font=("Montserrat Semibold", 12), width=width)
    elif widget_type == 'textarea':
        entry = tk.Text(content_frame, font=("Montserrat Semibold", 12), width=width, height=4)
    elif widget_type == 'combo':
        entry = ttk.Combobox(content_frame, font=("Montserrat Semibold", 12), width=width, state="readonly")
        entry['values'] = ["Disciplina 1", "Disciplina 2", "Disciplina 3"]  # Exemplo de disciplinas
        
    entry.grid(row=row + 1, column=column, columnspan=colspan, padx=20, pady=(0, 10), sticky="ew")
    return entry

nome_entry = create_label_and_entry("Nome da turma:", 2, 0, colspan=2, width=20)
data_inicio_entry = create_label_and_entry("Data início:", 4, 0, width=15)
data_fim_entry = create_label_and_entry("Data fim:", 4, 1, width=15)
sigla_entry = create_label_and_entry("Sigla do curso:", 6, 0, width=15)
disciplina_entry = create_label_and_entry("Adicionar disciplinas:", 6, 1, width=15, widget_type='combo')
dias_nao_letivos_entry = create_label_and_entry("Dias não letivos:", 2, 3, width=15)
descricao_dia_entry = create_label_and_entry("Descrição do dia não letivo:", 4, 3, colspan=4, widget_type='textarea')
    
back_button = tk.Button(bg_canvas, text="Voltar", command=go_back, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12), bd=1)
back_button.place(relx=0.35, rely=0.85, anchor=tk.CENTER)

next_button = tk.Button(bg_canvas, text="Cadastrar", command=cadastrar_button_click, width=20, bg="white", fg="#004080", font=("Montserrat Semibold", 12), bd=1)
next_button.place(relx=0.65, rely=0.85, anchor=tk.CENTER)

logo_image = load_image("imgs/logo.png", 120, 60)

bg_canvas.create_image(50, 40, image=logo_image, anchor='nw')

root.mainloop()