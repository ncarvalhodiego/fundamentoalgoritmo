qnt = 0
soma = 0
print("(0 para resultados)")

while True:
    x = int(input("Insira o número para somar: "))
    if x == 0:
        print("Quantidade de números:", qnt)
        print("Soma:", soma)
        print("Média:", soma/qnt)
        break
    else:
        qnt += 1
        soma += x