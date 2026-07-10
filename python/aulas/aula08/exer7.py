n = int(input("Digite o tamanho da cruz: "))
m = n*2-1


if n > 10 or n < 1:
    print("Número inválido!")
else:
    for i in range(m):
        if i == n-1:
            for i in range(m):
                print("+", end=" ")
        else:
            for j in range(m):
                if j == n-1:
                    print("+", end=" ")
                else:
                    print(" ", end=" ")
        print()