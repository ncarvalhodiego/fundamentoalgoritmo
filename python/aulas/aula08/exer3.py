import math
def analise(lista):
    tamh = len(lista)
    soma = 0
    for i in range(tamh):
        soma += lista[i]
    media = soma/tamh


    maximo = lista[0]
    minimo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i

    for i in lista:
        if i < minimo:
            minimo = i

    lista.sort()
    mediana = lista[math.floor(tamh/2)]

    return media, mediana, minimo, maximo