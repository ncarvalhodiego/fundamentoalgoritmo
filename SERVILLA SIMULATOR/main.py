import time, math
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from PIL import Image, ImageTk
from telamain import telaMain


def telaInicio():
    janela.destroy()
    telaMain()


def telaMenu():
    # criando janela
    global janela
    janela = tk.Tk()
    janela.title("Servilla Simulator")
    janela.geometry("500x300")


    # Carrega a imagem original
    imagem_original = Image.open("emojinerd.jpg")
    # Converte para PhotoImage
    foto = ImageTk.PhotoImage(imagem_original)
    # Cria o fundo
    fundo = tk.Label(janela, image=foto)
    fundo.image = foto  # mantém uma referência
    fundo.place(x=0, y=0, relwidth=1, relheight=1)
    # Redimensiona quando a janela muda de tamanho
    def redimensionar(event):
        nova = imagem_original.resize((event.width, event.height))
        foto = ImageTk.PhotoImage(nova)

        fundo.config(image=foto)
        fundo.image = foto
    janela.bind("<Configure>", redimensionar)


    # criando titulo
    title = tk.Label(text="    Jaoas Life    ", font=("Arial", 22, "bold"))
    title.pack(pady=(30,30))

    # criando botao de comecar 
    butao = tk.Button(janela, command=telaInicio, text="COMEÇAR", width=20, height=2)
    butao.pack(pady=(60,30))

#    if primeira vez entrando:
    messagebox.showinfo("Servilla Simulator", "Seja bem vindo ao simulador de Jaoas!!! Aqui você sobe de nível, toma suas próprias escolhas, cai, levanta, aprende a amar, a odiar, infarta, e principalmente... farma aura (rsrs)")
    messagebox.showinfo("Servilla Simulator", "Boa sorte, novo Jaoas...")
    
    # loop da janela
    janela.mainloop()
telaMenu()