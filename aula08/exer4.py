n = int(input(""))

totalcobaias = []
tipocobaias = []

for i in range(n):
    x = int(input(""))
    totalcobaias.append(x)
    y = str(input(""))
    tipocobaias.append(y)

soma = 0
for i in range(n):
    soma += totalcobaias[i]

tipocobaiascopia = tipocobaias
totalcoelhos = 0
for i in range(tipocobaiascopia.count("C")):
    posic = tipocobaiascopia.index("C")
    totalcoelhos += totalcobaias[posic]
    totalcobaias.pop(posic)
    tipocobaiascopia.pop(posic)

totalratos = 0
for i in range(tipocobaiascopia.count("R")):
    posic = tipocobaiascopia.index("R")
    totalratos += totalcobaias[posic]
    totalcobaias.pop(posic)
    tipocobaiascopia.pop(posic)

totalsapos = 0
for i in range(tipocobaiascopia.count("S")):
    posic = tipocobaiascopia.index("S")
    totalsapos += totalcobaias[posic]
    totalcobaias.pop(posic)
    tipocobaiascopia.pop(posic)



print("Total: %d cobaias" % soma)
print("Total de coelhos: %d" % totalcoelhos)
print("Total de ratos: %d" % totalratos)
print("Total de sapos: %d" % totalsapos)
print("Percentual de coelhos: %.2f %%" % (100/soma*totalcoelhos))
print("Percentual de ratos: %.2f %%" % (100/soma*totalratos))
print("Percentual de sapos: %.2f %%" % (100/soma*totalsapos))