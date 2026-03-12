x = int(input("Primeiro nº:"))
y = int(input("Segundo nº:"))
def multiplo(a,b):
    if b%a == 0:
        return("True")
    else:
        return("False")
print(multiplo(x,y))