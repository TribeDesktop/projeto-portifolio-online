
import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from disciplinas_backend import list_turma, list_curso
import subprocess

class ToplevelAlterar:
    def __init__(self, top=None, disciplina_id=None, dados=None):
        # Definir o tamanho da janela
        window_width = 1231
        window_height = 659

        # Calcular as coordenadas para centralizar a janela
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Configurações da janela principal
        top.geometry(f"{window_width}x{window_height}+{x}+{y}")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Editar Disciplina")
        top.configure(background="#d9d9d9")

        self.top = top

        
        #canvas gradiente
        self.canvas = tk.Canvas(self.top)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.update_gradient)
        
        #widgets da tela de alteração
        self.create_widgets(dados)
        
        self.disciplina_id = disciplina_id
        
        #função de popular os campos no inicio da aplicação
        self.populate_fields()
        
    def create_widgets(self, dados):
        # Frame para os campos de entrada
        self.TFrame1 = tk.Frame(self.top, bg="white")
        self.TFrame1.place(relx=0.179, rely=0.228, relheight=0.581, relwidth=0.605)
        self.TFrame1.configure(relief='groove', borderwidth="2")

        

        # Carrega a imagem e coloca no frame central
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


        #Funão para verificar se os caracteres são numeros
        def validate_number(P):
            if P.isdigit() or P == '':
                return True
            else:
                return False
        # Campos de entrada
        self.label_disciplina = tk.Label(self.TFrame1, text='Disciplina:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_disciplina.place(relx=0.121, rely=0.078, height=21, width=64)
        self.txt_disciplina = ttk.Entry(self.TFrame1)
        self.txt_disciplina.place(relx=0.121, rely=0.131, relheight=0.055, relwidth=0.3)


        self.label_sigla = tk.Label(self.TFrame1, text='Sigla:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_sigla.place(relx=0.121, rely=0.235, height=21, width=35)
        self.txt_sigla = ttk.Entry(self.TFrame1)
        self.txt_sigla.place(relx=0.121, rely=0.287, relheight=0.055, relwidth=0.3)


        self.label_aulas_semanais = tk.Label(self.TFrame1, text='Aulas Semanais:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_aulas_semanais.place(relx=0.121, rely=0.392)
        self.txt_aulas_semanais = ttk.Entry(self.TFrame1, validate="key", validatecommand=(root.register(validate_number), '%P'))
        self.txt_aulas_semanais.place(relx=0.121, rely=0.444, relheight=0.055, relwidth=0.3)

        self.label_total_aulas = tk.Label(self.TFrame1, text='Total de Aulas(Semestre):', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_total_aulas.place(relx=0.121, rely=0.548, height=21, width=135)
        self.txt_total_aulas = ttk.Entry(self.TFrame1, validate="key", validatecommand=(root.register(validate_number), '%P'))
        self.txt_total_aulas.place(relx=0.121, rely=0.601, relheight=0.055, relwidth=0.3)

        #carga horária
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
        
        #Disciplina ID combobox
        self.label_turmaid = tk.Label(self.TFrame1, text='Turma ID:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_turmaid.place(relx=0.564, rely=0.078, height=21, width=60)
        self.combobox_turmaid = ttk.Combobox(self.TFrame1, validate="key", state="readonly")
        self.combobox_turmaid.place(relx=0.564, rely=0.131, relheight=0.055, relwidth=0.1)
        
        #Lista curso
        self.label_cursoid = tk.Label(self.TFrame1, text='Curso ID:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_cursoid.place(relx=0.564, rely=0.185, height=21, width=60)
        self.combobox_cursoid = ttk.Combobox(self.TFrame1, validate="key", state="readonly")
        self.combobox_cursoid.place(relx=0.564, rely=0.251, relheight=0.055, relwidth=0.1)
        
        self.label_ementa = tk.Label(self.TFrame1, text='Ementa:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_ementa.place(relx=0.564, rely=0.350, height=21, width=55)
        self.txt_ementa = tk.Text(self.TFrame1)
        self.txt_ementa.place(relx=0.564, rely=0.420, height=140, relwidth=0.381)
        
         # Preencher Combobox com Turmas ids
        turma = list_turma()
        self.combobox_turmaid['values'] = [
            f"{turm[0]} - {turm[1]}" for turm in turma]

        # Preencher Combobox com Cursos ids
        curso = list_curso()
        self.combobox_cursoid['values'] = [
            f"{curs[0]} - {curs[1]}" for curs in curso]
        
        # Botão Alterar
        self.Button1 = tk.Button(self.TFrame1, text='Alterar', command=self.alterar_dados)
        self.Button1.place(relx=0.698, rely=0.888, height=26, width=77)

        self.divisoria = tk.Frame(self.TFrame1, bg="#2C5FA3")
        self.divisoria.place(relx=0.5, rely=0.5, relwidth=0.005, relheight=1, anchor=tk.CENTER)


        #fechar programa
        def fechar_programa():
            try:
                root.destroy()  # Fecha a janela atual  
            except Exception as e:
                print(f"Erro ao executar tarefa: {e}")
        self.Fechar = tk.Button(root, text="⬅️", font=("Montserrat", 18), bg="white", fg="#004080",command=fechar_programa)
        self.Fechar.place(x=10, y=10)
        
        # Adicionando imagem logo (opcional)
        self.add_small_image()

    def update_gradient(self, event=None):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.draw_gradient(width, height)

    def draw_gradient(self, width, height):
        # Definindo as cores do gradiente
        start_color = "#26A7B9"
        end_color = "#331C8F"

        # Criar o gradiente no Canvas
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

        # Redesenha o título ao atualizar o gradiente
        self.draw_title("Editar Disciplina")

    def draw_title(self, titulo):
        # Apaga o título anterior
        self.canvas.delete("titulo")
        
        width = self.canvas.winfo_width()
        x_position = width / 2  
        
        # Titulo no canvas
        self.canvas.create_text(x_position, 50, text=titulo, font=("Montserrat", 25, "bold"), fill="white", tags="titulo")

    def hex_to_rgb(self, hex_color):
        # Converte uma cor hexadecimal em RGB
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def verificar_campos_vazios(self):
        # Verifica se os campos estão vazios
            if not self.txt_disciplina.get():
                messagebox.showwarning("Campo Vazio", "O campo 'Disciplina' não pode estar vazio.")
                return False
            if not self.txt_sigla.get():
                messagebox.showwarning("Campo Vazio", "O campo 'Sigla' não pode estar vazio.")
                return False
            if not self.txt_aulas_semanais.get():
                messagebox.showwarning("Campo Vazio", "O campo 'Aulas Semanais' não pode estar vazio.")
                return False
            if not self.txt_total_aulas.get():
                messagebox.showwarning("Campo Vazio", "O campo 'Total de Aulas' não pode estar vazio.")
                return False
            if not self.txt_carga_horaria.get():
                messagebox.showwarning("Campo Vazio", "O campo 'Carga Horária' não pode estar vazio.")
                return False
            if not self.txt_ementa.get('1.0', 'end').strip():
                messagebox.showwarning("Campo Vazio", "O campo 'Ementa' não pode estar vazio.")
                return False
            if not self.combobox_cursoid.get():
                messagebox.showwarning("Campo Vazio", "O campo 'Curso ID' não pode estar vazio.")
                return False
            if not self.combobox_turmaid.get():
                messagebox.showwarning("Campo Vazio", "O campo 'Turma ID' não pode estar vazio.")
                return False
            return True
    
    def add_small_image(self):
        logo_path = os.path.join(os.path.dirname(__file__), 'imgs', 'logo.png')
        try:
            small_img = Image.open(logo_path)
            small_img = small_img.resize((100, 50))  
            small_img_tk = ImageTk.PhotoImage(small_img)

            # Adiciona a imagem ao frame inferior
            label_logo = tk.Label(self.top, image=small_img_tk, bg="#312593")  
            label_logo.image = small_img_tk  
            label_logo.place(relx=0.48, rely=0.85, anchor=tk.N) 
        except Exception as e:
            print(f"Erro ao carregar a imagem logo.png: {e}")
            print(f"Tentando carregar imagem de: {logo_path}")


    def formatar_carga_horaria(self, carga_horaria):
        """
        Recebe uma string no formato 'X day(s), HH:MM:SS' e retorna uma string formatada 'HH:MM'.
        """
        # Inicializa as variáveis
        dias = 0
        horas = 0
        minutos = 0

        # Tenta dividir a string em partes
        try:
            # Divide a string em partes separadas por vírgulas
            partes = carga_horaria.split(',')
            if len(partes) == 2:
                # Obtém os dias
                dias_partes = partes[0].strip().split()
                if len(dias_partes) > 0:
                    dias = int(dias_partes[0]) 

                # Obtém as horas e minutos da segunda parte
                horas_minutos = partes[1].strip().split(':')
                if len(horas_minutos) >= 2:
                    horas = int(horas_minutos[0])
                    minutos = int(horas_minutos[1])

        except Exception as e:
            print(f"Erro ao processar carga_horaria: {e}")

        # Converte dias em horas e soma com as horas restantes
        total_horas = dias * 24 + horas
        return f"{total_horas}:{minutos:02d}"

    def populate_fields(self):
        try:
            response = requests.get(f"http://localhost:8080/disciplinas?disciplinaID={self.disciplina_id}")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    data = data[0]
                    
                    # Obtém e formata a carga horária
                    carga_horaria = data.get("cargaHorariaDisciplina", "")

                    carga_horaria_formatada = self.formatar_carga_horaria(carga_horaria)
          
                     
                    
                    # Preenchendo os campos
                    self.txt_disciplina.insert(0, data.get("nomeDisciplina", ""))
                    self.txt_sigla.insert(0, data.get("siglaDisciplina", ""))
                    self.txt_aulas_semanais.insert(0, data.get("aulasSemanaisDisciplina", ""))
                    self.txt_total_aulas.insert(0, data.get("aulasTotaisSemestreDisciplina", ""))
                    self.txt_carga_horaria.insert(0, carga_horaria_formatada)
                    self.txt_ementa.insert("1.0", data.get("ementa", ""))
                    self.combobox_turmaid.set(data.get("turmaID", "")) 
                    self.combobox_cursoid.set(data.get("cursoID", ""))  
            else:
                messagebox.showerror("Erro", f"Erro ao carregar dados da disciplina: {response.text}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro de Conexão", f"Erro ao tentar carregar dados da disciplina: {str(e)}")

    def alterar_dados(self):
        if not self.verificar_campos_vazios():
            return
        data = {
            "disciplinaID": self.disciplina_id,
            "nomeDisciplina": self.txt_disciplina.get(),
            "siglaDisciplina": self.txt_sigla.get(),
            "aulasSemanaisDisciplina": int(self.txt_aulas_semanais.get()),
            "aulasTotaisSemestreDisciplina": int(self.txt_total_aulas.get()),
            "cargaHorariaDisciplina": self.txt_carga_horaria.get(),
            "ementa": self.txt_ementa.get("1.0", "end-1c"),
            "turmaID": self.combobox_turmaid.get(),
            "cursoID": self.combobox_cursoid.get()
        }

        try:
            response = requests.put("http://localhost:8080/disciplinas", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Disciplina atualizada com sucesso!")
                self.top.destroy()
            else:
                messagebox.showerror("Erro", f"Erro ao atualizar disciplina: {response.text}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro de Conexão", f"Erro ao tentar atualizar a disciplina: {str(e)}")

if __name__ == "__main__":
    disciplina_id = sys.argv[1] if len(sys.argv) > 1 else None
    root = tk.Tk()
    app = ToplevelAlterar(root, disciplina_id=disciplina_id)
    root.mainloop()
