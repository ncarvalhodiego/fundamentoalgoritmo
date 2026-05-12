x = int(input("Insira um número de 1 a 10: "))
if x <= 10 and x >= 1:
    print("Número aceito.")
else:
    while x > 10 or x < 1:
        print("Número inválido.")
        x = int(input("Insira um número de 1 a 10: "))
print("Número aceito.")