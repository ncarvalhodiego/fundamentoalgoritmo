import math
x = float(input("Primeiro nº: "))
y = float(input("Segundo nº: "))
z = float(input("Terceiro nº: "))
def conta(n1,n2,n3):
    res = (math.sqrt(n1)) + (math.sqrt(n2)) + (math.sqrt(n3)) + ((n1+n2)/2) + ((n2+n3)/2) + ((n1+n3)/2)
    return(res)
print(conta(x,y,z))