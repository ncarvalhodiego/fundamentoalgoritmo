z = int(input("Digite um número de 1 a 10: "))

if z >= 10 or z <=1:
    print("Número inválido!")
else:
    for i in range(z):
        for j in range(z):
            if i == j or i == z - j - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()