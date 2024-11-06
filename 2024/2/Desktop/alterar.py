import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import requests

class ToplevelAlterar:
    def __init__(self, top=None, disciplina_id=None):
        self.top = top
        self.disciplina_id = disciplina_id
        self.setup_window()
        self.create_widgets()
        self.populate_fields()

    def setup_window(self):
        window_width = 1231
        window_height = 659
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.top.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.top.title("Editar Disciplina")
        
        # Configuração do Canvas para o gradiente
        self.canvas = tk.Canvas(self.top, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.create_gradient(self.canvas, window_width, window_height, (0, 142, 179), (60, 33, 121))

        # Adiciona o frame sobre o canvas com fundo transparente
        self.TFrame1 = tk.Frame(self.canvas, bg="white")
        self.TFrame1.place(relx=0.179, rely=0.228, relheight=0.581, relwidth=0.605)

    def create_gradient(self, canvas, width, height, color1, color2):
        # Cria um gradiente de cima para baixo
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        for i in range(height):
            r = int(r1 + (r2 - r1) * i / height)
            g = int(g1 + (g2 - g1) * i / height)
            b = int(b1 + (b2 - b1) * i / height)
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_line(0, i, width, i, fill=color)

    def create_widgets(self):
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
        self.txt_aulas_semanais = ttk.Entry(self.TFrame1)
        self.txt_aulas_semanais.place(relx=0.121, rely=0.444, relheight=0.055, relwidth=0.3)

        self.label_total_aulas = tk.Label(self.TFrame1, text='Total de Aulas(Semestre):', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_total_aulas.place(relx=0.121, rely=0.548, height=21, width=135)
        self.txt_total_aulas = ttk.Entry(self.TFrame1)
        self.txt_total_aulas.place(relx=0.121, rely=0.601, relheight=0.055, relwidth=0.3)

        self.label_carga_horaria = tk.Label(self.TFrame1, text='Carga Horária:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_carga_horaria.place(relx=0.121, rely=0.705, height=21, width=85)
        self.txt_carga_horaria = ttk.Entry(self.TFrame1)
        self.txt_carga_horaria.place(relx=0.121, rely=0.757, relheight=0.055, relwidth=0.3)

        self.label_ementa = tk.Label(self.TFrame1, text='Ementa:', font="Montserrat 8", bg="white", fg="#2C5FA3")
        self.label_ementa.place(relx=0.564, rely=0.350, height=21, width=55)
        self.txt_ementa = tk.Text(self.TFrame1)
        self.txt_ementa.place(relx=0.564, rely=0.420, height=140, relwidth=0.381)

        # Botão para salvar alterações
        self.Button1 = tk.Button(self.TFrame1, text='Alterar', command=self.alterar_dados)
        self.Button1.place(relx=0.698, rely=0.888, height=26, width=77)

    def populate_fields(self):
        try:
            response = requests.get(f"http://localhost:8080/disciplinas?disciplinaID={self.disciplina_id}")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    data = data[0]
                self.txt_disciplina.insert(0, data.get("nomeDisciplina", ""))
                self.txt_sigla.insert(0, data.get("siglaDisciplina", ""))
                self.txt_aulas_semanais.insert(0, data.get("aulasSemanaisDisciplina", ""))
                self.txt_total_aulas.insert(0, data.get("aulasTotaisSemestreDisciplina", ""))
                self.txt_carga_horaria.insert(0, data.get("cargaHorariaDisciplina", ""))
                self.txt_ementa.insert("1.0", data.get("ementa", ""))
            else:
                messagebox.showerror("Erro", f"Erro ao carregar dados da disciplina: {response.text}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro de Conexão", f"Erro ao tentar carregar dados da disciplina: {str(e)}")

    def alterar_dados(self):
        data = {
            "disciplinaID": self.disciplina_id,
            "nomeDisciplina": self.txt_disciplina.get(),
            "siglaDisciplina": self.txt_sigla.get(),
            "aulasSemanaisDisciplina": int(self.txt_aulas_semanais.get()),
            "aulasTotaisSemestreDisciplina": int(self.txt_total_aulas.get()),
            "cargaHorariaDisciplina": int(self.txt_carga_horaria.get()),
            "ementa": self.txt_ementa.get("1.0", "end-1c")
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
