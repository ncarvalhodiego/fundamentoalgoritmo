print("Informe 10 números para obter a soma.")
contador = int(1)
acum = int(0)
while contador <= 10:
    print("Informe o", contador, "º número:")
    x=int(input(""))
    contador += 1
    acum += x
print("Resultado da soma:", acum)