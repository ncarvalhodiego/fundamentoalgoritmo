carros = []
consu = []

for i in range(5):
    x = str(input(""))
    carros.append(x)

for i in range(5):
    y = int(input(""))
    consu.append(y)

maior = consu[0]
xtr = 100
indice = i

for i in consu:
    if i > maior:
        maior = i
        indice = consu.index(maior)

print(carros[indice])
print(round(1000/consu[0]))
print(round(1000/consu[1]))
print(round(1000/consu[2]))
print(round(1000/consu[3]))
print(round(1000/consu[4]))