import os
import platform
import time

def limparTerminal():
    os.system("cls")

t = 0.05
def adeus():
    i = 0
    x = 3
    while i < x:
        limparTerminal()
        print("/")
        time.sleep(t)
        limparTerminal()
        print("-")
        time.sleep(t)
        limparTerminal()
        print("\\")
        time.sleep(t)
        limparTerminal()
        print("|")
        time.sleep(t)
        i+=1
    limparTerminal()