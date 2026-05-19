import msvcrt
import random

#print("Pressione uma tecla...")
#tecla = msvcrt.getch()
#print("Você pressionou:", tecla.decode())
#print(random.randint(1,10))

#lista = ["Titulo", "Canal", "Duracao", "DataLancamento", "Genero"]
#print(lista)

#with open("videos.txt", "a") as videos:
#    videos.write("%s\%s\%s\%s\%s\n" % (lista[0], lista[1], lista[2], lista[3], lista[4]))

with open("videos.txt", "r") as videos:
    lista = []
    nome = str(input(">> "))
    for linha in videos.readlines(): 
        linhaa = linha.strip().split("\\")
        if linhaa[0] == nome:
            print(linhaa, "- Encontrado!")