par = open("pares.txt" , "w")
impar = open("impares.txt" , "w")

for linha in range(0,999):
    if linha % 2 == 0:
        par.write("%d\n" %linha)
    elif linha % 2 != 0:
        impar.write("%d\n" %linha)
par.close()
impar.close()