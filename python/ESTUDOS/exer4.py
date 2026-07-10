import os
import platform
os.system("cls")

matriz = []

#criar a matriz
for i in range(3):
    linha = []
    for j in range(3):
        x = int(input("Digite o input: "))
        linha.append(x)
    matriz.append(linha)

#mostrar a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print("%3d" % (matriz[i][j]), end=" ")
    print()

#calcular diagonais
soma = 0
produto = 1
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            soma = soma + (matriz[i][j])
            produto = produto*(matriz[i][j])

print("Soma da diagonal: %d" % soma)
print("Produto da diagonal: %d" % produto)