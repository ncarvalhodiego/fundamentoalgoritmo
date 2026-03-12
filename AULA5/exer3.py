x = int(input("Primeiro nº:"))
y = int(input("Segundo nº:"))
def maximo(a,b):
    if a > b:
        return(a)
    else:
        return(b)
print(maximo(x,y))