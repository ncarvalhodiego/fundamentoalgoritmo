import math
salario = 5075.0

ano = int(input("Digite o ano desejado: "))
tempo = ano - 2007

t = 0.015
for i in range(2006, ano):
    t = t*2
    salario = salario + salario * t

print("Salário de %d: R$ %.2f" % (ano, salario))