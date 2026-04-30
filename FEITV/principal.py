import os
import platform
import time
import msvcrt
import random

usuario = ""

def limparTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def adeus():
    t = 0.2
    print("Adeus!")
    time.sleep(t)
    limparTerminal()
    print("Adeus")
    time.sleep(t)
    limparTerminal()
    print("Adeu")
    time.sleep(t)
    limparTerminal()
    print("Ade")
    time.sleep(t)
    limparTerminal()
    print("Ad")
    time.sleep(t)
    limparTerminal()
    print("A")
    time.sleep(t)
    limparTerminal()

def formatarUsers():
    novasLinhas = []
    with open("usuarios.txt" , "r") as users:
        for linha in users.readlines():
            linhaa = linha.strip().split()
            if len(linhaa) > 1:
                novasLinhas.append(linha)
    with open ("usuarios.txt" , "w") as users:
        users.writelines(novasLinhas)

def explorar():
    print()
    with open("videos.txt" , "r") as videos:
        linhas = videos.readlines()
        nLinhas = len(linhas)
        for i in range(10):
            num = random.randint(1,nLinhas)
            linhasss = linhas[num-1].strip().split("\\")
            print("%s --> %s" % (linhasss[0],linhasss[1]))
            print()

def menu():
    limparTerminal()
    print("MENU  -  Bem vindo/a, %s!" % usuario)
    print()
    print("1 - Pesquisar (por nome)")
    print("2 - Gerenciar favoritos")
    print("0 - Sair")
    print()
    print("Explorar:")
    explorar()

def paginaLogin():
    sucess = False
    usuarioInp = str(input("Usuário: "))
    senhaInp = str(input("Senha: "))
    with open("usuarios.txt" , "r") as users:
        for linha in users.readlines():
            linhaa = linha.strip().split()
            if linhaa[0] == usuarioInp and linhaa[1] == senhaInp:
                global usuario
                usuario = linhaa[0]
                sucess = True
    if sucess:
        menu()
    else:
        print()
        print("Usuário ou senha incorretos!")
        time.sleep(2)
        paginaInicial()

def paginaSigin():
    limparTerminal()
    print("Crie o nome de usuário:   (enter para voltar)")
    usuarior = str(input(">> "))
    usuario = usuarior.strip()
    if usuario == "":
        paginaInicial()
    else:
        jaExiste = False
        with open("usuarios.txt" , "r") as users:
            for linha in users.readlines():
                linhaa = linha.strip().split()
                if linhaa[0] == usuario:
                    jaExiste = True
        if jaExiste == True:
            print("Esse nome de usuário ja existe!")
            time.sleep(2)
            limparTerminal()
            paginaInicial()
        else:            
            usersplit = usuario.strip().split()
            if len(usersplit) > 1:
                print("O nome de usuário não pode conter espaços!")
                time.sleep(2)
                paginaInicial()
            else:
                limparTerminal()
                print("Digite a senha: ")
                senha1 = str(input(">> "))
                print("Confirme a senha: ")
                senha2 = str(input(">> "))
                senhaa = senha1.strip().split()
                if len(senhaa) > 1:
                    print("A senha não pode conter espaços!")
                    time.sleep(2)
                    paginaInicial()
                else:
                    if senha1 == senha2:
                        with open("usuarios.txt" , "a") as usuarios:
                            usuarios.write("%s %s\n" % (usuario.strip(), senha1.strip()))
                        print("Usuário criado!")
                        time.sleep(1)
                        print("Você ja pode fazer login!")
                        time.sleep(2)
                        paginaInicial()
                    else:
                        print("As senhas não batem!")
                        time.sleep(2)
                        paginaInicial()

def paginaInicial():
    limparTerminal()
    print("Bem Vindo ao FeiTV!")
    print()
    print("1 - Login")
    print("2 - Signin")
    print("0 - Sair")
    print()
    inp = msvcrt.getch().decode()
    if inp == "1":
        paginaLogin()
    elif inp == "2":
        paginaSigin()
    elif inp == "0":
        limparTerminal()
        adeus()
    else:
        paginaInicial()

paginaInicial()