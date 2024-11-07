from tkinter import *
from PIL import Image, ImageTk
from messages_back import Msg
import os


# Função para gerar um gradiente entre duas cores
def gerar_gradiente(canvas, largura, altura, cor1, cor2, steps=100):
    r1, g1, b1 = canvas.winfo_rgb(cor1)  # RGB da cor 1
    r2, g2, b2 = canvas.winfo_rgb(cor2)  # RGB da cor 2

    # Normalizando as cores para [0, 255]
    r1, g1, b1 = r1 // 256, g1 // 256, b1 // 256
    r2, g2, b2 = r2 // 256, g2 // 256, b2 // 256

    for i in range(steps):
        # Interpolando entre as duas cores
        r = int(r1 + (r2 - r1) * i / steps)
        g = int(g1 + (g2 - g1) * i / steps)
        b = int(b1 + (b2 - b1) * i / steps)

        # Convertendo para a cor hexadecimal
        cor_interpolada = f'#{r:02x}{g:02x}{b:02x}'
        
        # Desenhando uma faixa no canvas para gradiente
        canvas.create_rectangle(0, i * altura // steps, largura, (i + 1) * altura // steps, outline="", fill=cor_interpolada)

# Função para atualizar o texto da label
def atualizar_titulo(canvas, titulo):
    canvas.delete("titulo")  # Remove o texto antigo
    canvas.create_text(525, 145, text=titulo, font=("Montserrat", 33, "bold"), fill="white", tags="texto")
    
def atualizar_mensagem(canvas, msg):
    canvas.delete("msg")  # Remove o texto antigo
    canvas.create_text(525, 200, text=msg, font=("Montserrat", 17, "bold"), fill="white", tags="texto")
    
# Função para carregar e redimensionar imagem
def carregar_imagem(caminho, largura, altura):
    caminho = os.path.join(os.path.dirname(__file__), caminho)
    imagem = Image.open(caminho)
    imagem_redimensionada = imagem.resize((largura, altura), Image.LANCZOS)
    return ImageTk.PhotoImage(imagem_redimensionada)

# Função principal que exibe o popup
def exibir_popup(titulo, mensagem):
    # Criar a janela principal
    janela = Tk()
    janela.title("Atenção!")

        # Função para fechar a janela
    def quit():
        janela.destroy()
    
    # Define o tamanho da tela
    janela.geometry("800x400")
    janela.resizable(True, True)
    janela.maxsize(width=1920, height=1080)
    janela.minsize(width=300, height=300)

    # Criar o canvas para desenhar o gradiente
    canvas = Canvas(janela, width=800, height=400, bg='black', highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Definir as cores do gradiente
    cor1 = "#26a7b9"  
    cor2 = "#331c8f"  

    # Gerar o gradiente
    gerar_gradiente(canvas, 800, 400, cor1, cor2)

    # Carregar a imagem
    img_retangulo = carregar_imagem("./imgs/fig_retangulo.png", 60, 190)  
    img_logo = carregar_imagem("./imgs/logo2_escola.png", 160, 65)

    # Adicionar a imagem ao Canvas
    canvas.create_image(120, 0, image=img_retangulo, anchor='nw') 
    canvas.create_image(85, 280, image=img_logo, anchor='nw') 

    # Atualizar o título e a mensagem com os parâmetros recebidos
    atualizar_titulo(canvas, titulo)
    atualizar_mensagem(canvas, mensagem)
    
    # Botão fechar
    btn_fechar = Button(janela, text="Fechar", bg="#FFFFFF", fg="#331c8f", width=25, height=1, font=("Montserrat", 12, "bold"), command=quit)
    btn_fechar.place(x=400, y=250)
    
    # Função para restaurar a cor original ao sair com o mouse
    def on_leave(e):
        btn_fechar['background'] = '#FFFFFF'  # Cor de fundo original

    # Função para mudar a cor do botão ao passar o mouse
    def on_enter(e):
        btn_fechar['background'] = '#D9D9D9'  # Muda a cor de fundo ao passar o mouse

    
    btn_fechar.bind("<Enter>", on_enter)  # Quando o mouse entra no botão
    btn_fechar.bind("<Leave>", on_leave)  # Quando o mouse sai do botão
        

    # Executa a tela
    janela.mainloop()



