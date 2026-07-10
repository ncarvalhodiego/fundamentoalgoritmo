import os
import platform
os.system("cls")
import math
import random

a = int(input(">> "))
b = int(input(">> "))

matriz = []

#criar matriz
for i in range(a):
    linha = []
    for j in range(b):
        x = random.randint(0,9)
        linha.append(x)
    matriz.append(linha)

#printar matriz normal
for i in range(a):
    for j in range(b):
        print("%2d" % matriz[i][j], end=" ")
    print()

#criar matriz transposta
tmatriz = []
for i in range(b):
    linha = []
    for j in range(a):
        x = matriz[j][i]
        linha.append(x)
    tmatriz.append(linha)

print()
print()

#printar matriz transposta
for i in range(b):
    for j in range(a):
        print("%2d" % tmatriz[i][j], end=" ")
    print()