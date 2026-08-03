import time, math
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from PIL import Image, ImageTk


def apertou():
    print("apertou")


def criarBotao(texto, funcao, x, y):
    botao = tk.Button(janela, command=funcao, text=texto, width=10, height=3, font=("Arial", 14, "bold"))
    botao.pack()
    botao.place(x=x, y=y)


def telaMain():
    global janela
    janela = tk.Tk()
    janela.title("Servilla Simulator")
    janela.geometry("700x500")

    criarBotao("APERTE", apertou, 50, 110)
    criarBotao("PENIS\nGROSSO", apertou, 400, 250)