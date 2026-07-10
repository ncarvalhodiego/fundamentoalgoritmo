n = 1
soma = 1/n

x = int(input("Insira um número: "))
y = x + 1

while n < y:
    print(soma)
    soma += 1/n
    n += 1

print(soma)