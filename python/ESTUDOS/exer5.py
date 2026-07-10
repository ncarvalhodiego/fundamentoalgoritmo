import os
import platform
os.system("cls")

matriz = []

#criar matriz
for i in range(4):
    linha = []
    for j in range(4):
        x = int(input("Digite o input: "))
        linha.append(x)
    matriz.append(linha)

#printar matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print("%3d" % matriz[i][j], end=" ")
    print()

#somar os impares
somas = []
for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[0])):
        x = matriz[i][j]
        if x % 2 != 0:
            soma += x
    somas.append(soma)

print("Soma dos impares por linha:", somas)