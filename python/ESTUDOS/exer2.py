from random import random, randint
import math
import os
import platform
os.system("cls")

inteiros = []
reais = []
strings = ["pinto, coco, xixi, bunda, bosta, liquida, seveeeen"]

while len(inteiros) < 10:
    x = randint(1,1000)
    inteiros.append(x)
while len(reais) < 5:
    x = random()
    x = x*100000
    x = math.trunc(x)
    x = x/100
    reais.append(x)

print(inteiros)
print(reais)
print(strings)

total = []
total.append(inteiros)
total.append(reais)
total.append(strings)

del inteiros
del reais
del strings

print(total)