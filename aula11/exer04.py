invertido = open("invertido.txt", "w")
pares = open("pares.txt", "r")
quantidade = sum(1 for i in pares.readlines())

linhas = pares.readlines()
linhasinvertidas = linhas[::-1]
invertido.writelines(linhasinvertidas)