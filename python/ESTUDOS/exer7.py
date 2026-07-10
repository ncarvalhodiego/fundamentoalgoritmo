import os, platform, random, math
os.system("cls")


n = 12
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        x = random.randint(0,9)
        linha.append(x)
    matriz.append(linha)

for i in range(n):
    for j in range(n):
        print("%3d" % matriz[i][j], end="")
    print()
print()
print()

numeros = []
for i in range(n):
    for j in range(n):
        if i > j:
            numeros.append(matriz[i][j])

soma = 0
for i in range(len(numeros)):
    soma += numeros[len(numeros)-1]
    numeros.pop()

print("Soma do setor positivo do corte diagonal de cima p baixo sem incluir os números que passam pelo corte:", soma)
#q nome merda