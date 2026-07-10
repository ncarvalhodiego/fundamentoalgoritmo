import random
import math
import os
import platform
os.system("cls")
matriz = []

iii = int(input("Digite o número de colunas: "))
jjj = int(input("Digite o número de linhas: "))


for i in range(iii):
    coluna = []
    for j in range(jjj):
        x = random.random()
        x = x*100
        x = math.trunc(x)
        coluna.append(x)
    matriz.append(coluna)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        x = str("%d,%d" % (i,j))
        print("%4s" % x, end=" ")
    print()