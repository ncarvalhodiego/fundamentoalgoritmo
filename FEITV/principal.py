import os
import platform
from time import sleep
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
    sleep(t)
    limparTerminal()
    print("Adeus")
    sleep(t)
    limparTerminal()
    print("Adeu")
    sleep(t)
    limparTerminal()
    print("Ade")
    sleep(t)
    limparTerminal()
    print("Ad")
    sleep(t)
    limparTerminal()
    print("A")
    sleep(t)
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


def paginaVideo(video):
    limparTerminal()
    print("PAGINA VIDEO")
    print()

def paginaFavoritos():
    limparTerminal()
    print("FAVORITOS")
    with open("favoritos.txt" , "r") as favs:
        linhas = favs.readlines()
        for i in linhas:
            print(i)

def paginaPesquisar():
    limparTerminal()
    print("PESQUISA POR NOME:")
    pesq = str(input(">> "))


def explorar():
    print()
    with open("videos.txt" , "r") as videos:
        linhas = videos.readlines()
        nLinhas = len(linhas)
        for i in range(10):
            num = random.randint(6,nLinhas)
            linhasss = linhas[num-1].strip().split("\\")
            print("%s --> %s" % (linhasss[0],linhasss[1]))
            print()

def menu():
    limparTerminal()
    print("Bem vindo/a, %s!" % usuario)
    print()
    print("1 - Pesquisar (por nome)")
    print("2 - Gerenciar favoritos")
    print("0 - Sair")
    print()
    print("Explorar:")
    explorar()
    inp = msvcrt.getch().decode()
    if inp == "0":
        paginaInicial()
    if inp == "1":
        paginaPesquisar()
    if inp == "2":
        paginaFavoritos()
    else:
        menu()

def paginaLogin():
    formatarUsers()
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
        sleep(2)
        paginaInicial()

def paginaSigin():
    formatarUsers()
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
            sleep(2)
            limparTerminal()
            paginaInicial()
        else:            
            usersplit = usuario.strip().split()
            if len(usersplit) > 1:
                print("O nome de usuário não pode conter espaços!")
                sleep(2)
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
                    sleep(2)
                    paginaInicial()
                if len(senhaa) == 0:
                    print("A senha não pode ser nula!")
                    sleep(2)
                    paginaInicial()
                else:
                    if senha1 == senha2:
                        with open("usuarios.txt" , "a") as usuarios:
                            usuarios.write("%s %s\n" % (usuario.strip(), senha1.strip()))
                        print("Usuário criado!")
                        sleep(1)
                        print("Você ja pode fazer login!")
                        sleep(2)
                        paginaInicial()
                    else:
                        print("As senhas não batem!")
                        sleep(2)
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