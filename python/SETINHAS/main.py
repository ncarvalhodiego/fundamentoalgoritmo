import os, platform, msvcrt
def limparTerminal():
    os.system("cls")


lista = ["Python top", "Não sei inventar nomes", "vtnc deolane",
        "pum com bosta", "anoes malhados", "skibidi",
        "enzo é gay", "quero comer raspa de parede"]
k = 0

def menu():
    global k
    limparTerminal()
    n = 0
    for i in lista:
        print()
        if n == k:
            print(f">> {i}")
        else:
            print(f"   {i}") 
        n+=1
    print()
    x = msvcrt.getch()
    if x in (b'\x00', b'\xe0'):
        x = msvcrt.getch()
        if x == b'H' and k > 0:
            k -= 1
        elif x == b'P' and k < (len(lista) - 1):
            k += 1
    elif x.decode() == "e":
        print()
        print("VOCÊ ESCOLHEU: " + lista[k])
        print("...")
        print()
        return
    elif x.decode() == "q":
        return
    elif x.decode() == "x":
        lista.pop(k)
    menu()



menu()