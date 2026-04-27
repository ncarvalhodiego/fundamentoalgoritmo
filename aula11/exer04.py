invertido = open("invertido.txt", "w")
pares = open("pares.txt", "r")

linhas = pares.readlines()
linhasinvertidas = linhas[::-1]
invertido.writelines(linhasinvertidas)

invertido.close()
pares.close()