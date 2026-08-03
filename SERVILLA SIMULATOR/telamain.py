import time, math
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog


def criarBotao(texto, funcao, x, y):
    botao = tk.Button(janela, command=funcao, text=texto, width=10, height=3, font=("Arial", 14, "bold"))
    botao.pack()
    botao.place(x=x, y=y)


def telaMain():
    global janela
    janela = tk.Tk()
    janela.title("Servilla Simulator®")
    janela.geometry("700x500+30+30")

    titulo = tk.Label(text="   Jaoas Life   ", font=("Arial", 20, "bold"))
    titulo.pack(pady=(20,20))

    stats = tk.Label(text="Jaoas Stats")
    stats.pack()

    global botaomapa
    botaomapa = tk.Button(janela, command=telaMapa, text="MAPA", width=10, height=3, font=("Arial", 14, "bold"))
    botaomapa.pack()
    botaomapa.place(x=550, y=400)


def fecharmapa():
    janela2.destroy()
    botaomapa.place(x=550, y=400)


def telaMapa():
    botaomapa.place_forget()
    global janela2
    janela2 = tk.Toplevel(janela)
    janela2.title("Servilla Simulator®")
    janela2.geometry("700x400+750+60")

    titulo = tk.Label(janela2, text=("MAPA"), font=("Arial", 20, "bold"))
    titulo.pack(pady=(20,20))

    janela2.protocol("WM_DELETE_WINDOW", fecharmapa)