import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import requests  
from alterar import ToplevelAlterar
from disciplinas_backend import list_turma
from disciplinas_backend import list_curso
import subprocess


class Toplevel1:
    def __init__(self, top=None):
        # Define o tamanho da janela
        window_width = 1231
        window_height = 659

        # centralizar a janela
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Configurações da janela principal
        top.geometry(f"{window_width}x{window_height}+{x}+{y}")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Cadastrar Disciplina")
        top.configure(background="#d9d9d9")

        self.top = top

        # Adiciona um Canvas e desenha o gradiente de fundo
        self.canvas = tk.Canvas(self.top)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.update_gradient)

        # Cria os widgets da tela de cadastro
        self.create_widgets()

        
        marca_page_path = os.path.join(os.path.dirname(__file__), 'imgs', 'marca_page.png')
        try:
            img_marca_page = Image.open(marca_page_path)
            img_marca_page = img_marca_page.resize((30, 100)) 
            img_marca_page_tk = ImageTk.PhotoImage(img_marca_page)

            label_img = tk.Label(self.TFrame1, image=img_marca_page_tk, bg="white")
            label_img.image = img_marca_page_tk  
            label_img.place(relx=0.05, y=0.0, anchor=tk.N)  
        except Exception as e:
            print(f"Erro ao carregar a imagem marca_page.png: {e}")
            print(f"Tentando carregar imagem de: {marca_page_path}")

        # Desenha o título
        self.draw_title("Cadastrar Disciplina")

        self.add_small_image()
        
    def create_widgets(self):
        # Frame para os campos de entrada
        self.TFrame1 = tk.Frame(self.top, bg="white")
        self.TFrame1.place(relx=0.179, rely=0.228,
                           relheight=0.581, relwidth=0.605)
        self.TFrame1.configure(relief='groove', borderwidth="2")

        # Função para verificar se os caracteres são números
        def validate_number(P):
            if P.isdigit() or P == '':
                return True
            else:
                return False

        # Campos de entrada
        self.label_disciplina = tk.Label(
            self.TFrame1, text='Disciplina:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_disciplina.place(
            relx=0.121, rely=0.078, height=21, width=64)
        self.txt_disciplina = ttk.Entry(self.TFrame1)
        self.txt_disciplina.place(
            relx=0.121, rely=0.131, relheight=0.055, relwidth=0.3)

        self.label_sigla = tk.Label(
            self.TFrame1, text='Sigla:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_sigla.place(relx=0.121, rely=0.235, height=21, width=35)
        self.txt_sigla = ttk.Entry(self.TFrame1)
        self.txt_sigla.place(relx=0.121, rely=0.287,
                             relheight=0.055, relwidth=0.3)

        self.label_aulas_semanais = tk.Label(
            self.TFrame1, text='Aulas Semanais:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_aulas_semanais.place(
            relx=0.121, rely=0.405, height=21, width=85)
        self.txt_aulas_semanais = ttk.Entry(
            self.TFrame1, validate="key", validatecommand=(root.register(validate_number), '%P'))
        self.txt_aulas_semanais.place(
            relx=0.121, rely=0.457, relheight=0.055, relwidth=0.3)

        self.label_total_aulas = tk.Label(
            self.TFrame1, text='Total de Aulas(Semestre):', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_total_aulas.place(
            relx=0.121, rely=0.535, height=21, width=135)
        self.txt_total_aulas = ttk.Entry(self.TFrame1, validate="key", validatecommand=(
            root.register(validate_number), '%P'))
        self.txt_total_aulas.place(
            relx=0.121, rely=0.601, relheight=0.055, relwidth=0.3)

        def on_key_press(event):
            if event.keysym == "BackSpace":
                return
            if event.keysym == "Tab":
                return
            current_text = self.txt_carga_horaria.get()
            if len(current_text) == 2 and event.char.isdigit():
                self.txt_carga_horaria.insert(2, ':')
            elif len(current_text) > 4:
                return "break"  
            if not event.char.isdigit():
                return "break" 
        self.label_carga_horaria = tk.Label(
            self.TFrame1, text='Carga Horária: (hh:mm)', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_carga_horaria.place(
            relx=0.121, rely=0.705, height=21, width=140)
        self.txt_carga_horaria = ttk.Entry(self.TFrame1)
        self.txt_carga_horaria.place(
            relx=0.121, rely=0.757, relheight=0.055, relwidth=0.3)
        self.txt_carga_horaria.bind('<KeyPress>', on_key_press)
        
            # Lista de turma
        self.label_turmaid = tk.Label(
            self.TFrame1, text='Turma ID:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_turmaid.place(relx=0.564, rely=0.078, height=21, width=60)

        self.combobox_turmaid = ttk.Combobox(
            self.TFrame1, validate="key", state="readonly")
        self.combobox_turmaid.place(
            relx=0.564, rely=0.131, relheight=0.055, relwidth=0.1)

        # Lista curso
        self.label_cursoid = tk.Label(
            self.TFrame1, text='Curso ID:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_cursoid.place(relx=0.564, rely=0.185, height=21, width=60)

        self.combobox_cursoid = ttk.Combobox(
            self.TFrame1, validate="key", state="readonly")
        self.combobox_cursoid.place(
            relx=0.564, rely=0.251, relheight=0.055, relwidth=0.1)

        # Preencher Combobox com Turmas ids
        turma = list_turma()
        self.combobox_turmaid['values'] = [
            f"{turm[0]} - {turm[1]}" for turm in turma]

        # Preencher Combobox com Cursos ids
        curso = list_curso()
        self.combobox_cursoid['values'] = [
            f"{curs[0]} - {curs[1]}" for curs in curso]

        self.label_ementa = tk.Label(
            self.TFrame1, text='Ementa:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_ementa.place(relx=0.564, rely=0.350, height=21, width=55)
        self.txt_ementa = tk.Text(self.TFrame1)
        self.txt_ementa.place(relx=0.564, rely=0.420,
                              height=140, relwidth=0.381)

        # Botão Cadastrar
        self.Button1 = tk.Button(
            self.TFrame1, text='Cadastrar', command=self.salvar_dados)
        self.Button1.place(relx=0.698, rely=0.888, height=26, width=77)

        #Botão Fechar
        def fechar_programa():
            try:
                root.destroy()  # Fecha a janela atual
                subprocess.Popen(["python", "diciplina.py"])  # Abre a nova janela
            except Exception as e:
                print(f"Erro ao executar tarefa: {e}")
        self.Fechar = tk.Button(root, text="⬅️", font=("Montserrat", 18), bg="white", fg="#004080",command=fechar_programa)
        self.Fechar.place(x=10, y=10)

     

        # Divisória fina
        self.divisoria = tk.Frame(self.TFrame1, bg="#2C5FA3")
        self.divisoria.place(relx=0.5, rely=0.5,
                             relwidth=0.005, relheight=1, anchor=tk.CENTER)

    def update_gradient(self, event=None):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.draw_gradient(width, height)

    def draw_gradient(self, width, height):
        start_color = "#26A7B9"
        end_color = "#331C8F"

        gradient = tk.PhotoImage(width=width, height=height)
        for i in range(height):
            r1, g1, b1 = self.hex_to_rgb(start_color)
            r2, g2, b2 = self.hex_to_rgb(end_color)
            r = int(r1 + (r2 - r1) * i / height)
            g = int(g1 + (g2 - g1) * i / height)
            b = int(b1 + (b2 - b1) * i / height)
            color = f'#{r:02x}{g:02x}{b:02x}'
            gradient.put(color, (0, i, width, i + 1))

        self.canvas.create_image(0, 0, anchor=tk.NW, image=gradient)
        self.canvas.image = gradient

        self.draw_title("Cadastrar Disciplina")

    def draw_title(self, titulo):
        self.canvas.delete("titulo")
        width = self.canvas.winfo_width()
        x_position = width / 2
        self.canvas.create_text(x_position, 50, text=titulo, font=(
            "Montserrat", 25, "bold"), fill="white", tags="titulo")

    def add_small_image(self):
        logo_path = os.path.join(os.path.dirname(__file__), 'imgs', 'logo.png')
        try:
            small_img = Image.open(logo_path)
            small_img = small_img.resize((100, 50))
            small_img_tk = ImageTk.PhotoImage(small_img)
            label_logo = tk.Label(self.top, image=small_img_tk, bg="#312593")
            label_logo.image = small_img_tk
            label_logo.place(relx=0.48, rely=0.85, anchor=tk.N)
        except Exception as e:
            print(f"Erro ao carregar a imagem logo.png: {e}")

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def verificar_campos_vazios(self):
        if not self.txt_disciplina.get():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Disciplina' não pode estar vazio.")
            return False
        if not self.txt_sigla.get():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Sigla' não pode estar vazio.")
            return False
        if not self.txt_aulas_semanais.get():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Aulas Semanais' não pode estar vazio.")
            return False
        if not self.txt_total_aulas.get():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Total de Aulas' não pode estar vazio.")
            return False
        if not self.txt_carga_horaria.get():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Carga Horária' não pode estar vazio.")
            return False
        if not self.txt_ementa.get('1.0', 'end').strip():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Ementa' não pode estar vazia.")
            return False
        if not self.combobox_cursoid.get():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Curso ID' não pode estar vazio.")
            return False
        if not self.combobox_turmaid.get():
            messagebox.showwarning(
                "Campo Vazio", "O campo 'Turma ID' não pode estar vazio.")
            return False
        return True

    def salvar_dados(self):
        if not self.verificar_campos_vazios():
            return

        disciplina = self.txt_disciplina.get()
        sigla = self.txt_sigla.get()
        aulas_semanais = self.txt_aulas_semanais.get()
        total_aulas = self.txt_total_aulas.get()
        carga_horaria = self.txt_carga_horaria.get()

        ementa = self.txt_ementa.get('1.0', 'end').strip()
        turma = self.combobox_turmaid.get().split(' - ')[0]
        curso = self.combobox_cursoid.get().split(' - ')[0]

        data = {
            "nomeDisciplina": disciplina,
            "siglaDisciplina": sigla,
            "aulasSemanaisDisciplina": int(aulas_semanais),
            "aulasTotaisSemestreDisciplina": int(total_aulas),
            "cargaHorariaDisciplina": carga_horaria,
            "ementa": ementa,
            "turmaID": int(turma),
            "cursoID": int(curso)
        }

        try:
            response = requests.post(
                'http://localhost:8080/disciplinas', json=data)
            if response.status_code == 200:
                messagebox.showinfo(
                    "Sucesso", "Disciplina cadastrada com sucesso!")
                self.limpar_campos()
            else:
                messagebox.showerror(
                    "Erro", f"Falha ao cadastrar disciplina. Erro: {response.text}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror(
                "Erro de Conexão", f"Não foi possível conectar à API. Erro: {str(e)}")

    def limpar_campos(self):
        self.txt_disciplina.delete(0, tk.END)
        self.txt_sigla.delete(0, tk.END)
        self.txt_aulas_semanais.delete(0, tk.END)
        self.txt_total_aulas.delete(0, tk.END)
        self.txt_carga_horaria.delete(0, tk.END)
        self.txt_ementa.delete("1.0", tk.END)
        self.combobox_turmaid.set("")
        self.combobox_cursoid.set("")

    def abrir_alterar_tela(self):
        self.alterar_toplevel = ToplevelAlterar(self.top)


if __name__ == "__main__":
    root = tk.Tk()
    app = Toplevel1(root)
    root.mainloop()
