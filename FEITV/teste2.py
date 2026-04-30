from tkinter import *
window = Tk()

window.title("Nova tela")

window.geometry('350x200')

btn1 = Button(window, text = "Botao 1")
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn2 = Button(window, text = "Botao 2")
btn2.place(x = 100, y = 50, anchor = CENTER)

cliques = 0
def clique():
    global cliques
    cliques += 1
    print("CLICOU %d" %cliques)

botao = Button(window, text = "Clique aqui!", command=clique)
botao.place(x=200, y=200, anchor=CENTER)

window.mainloop()