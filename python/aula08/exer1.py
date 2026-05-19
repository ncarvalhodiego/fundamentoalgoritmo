lista = []
w = int(input("Digite o tamanho da lista: "))

for i in range(w):
    x = int(input("Digite um número: "))
    lista.append(x)

soma = 0
tamanho = len(lista)

for i in range(tamanho):
  soma += lista[i]

print(soma/tamanho)