import random
arquivo = open("numeros.txt", "w")

for i in range(100):
    n = random.randint(1,100)
    arquivo.write("%d " % n)

arquivo.close()

arquivo = open("numeros.txt", "r")

numeros = arquivo.read().strip().split()
soma = 0
for linha in numeros:
    soma += int(linha)

print(soma)

arquivo.close()