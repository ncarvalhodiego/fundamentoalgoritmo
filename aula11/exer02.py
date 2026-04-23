pares = open("pares.txt" , "r")
quad = open("quad.txt" , "w")

for linha in pares.readlines():
    if int(linha) % 4 == 0:
        quad.write("%d\n" % int(linha))

pares.close()
quad.close()