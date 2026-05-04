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

def adicionarFavs(midiaNome):
    print("ADICIONOU FAVORITO", midiaNome)

def paginaVideo(video):
    limparTerminal()
    print("Titulo: %s" % video[0])
    print("%s de %s" % (video[5], video[1]))
    print("Duração: %s" %video[2])
    print("Lançado em %s" %video[3])
    print("Tipo de midia: %s" %video[4])
    print()
    print("1 - Adicionar aos favoritos")
    print("0 - Voltar")
    inp = msvcrt.getch().decode()
    if inp == "1":
        adicionarFavs(video[0])
        print
        return
    else:
        menu()
        return

def paginaFavoritos():
    limparTerminal()
    print("FAVORITOS")

def paginaPesquisar():
    print("PESQUISA POR NOME:  (enter para voltar)")
    pesq = str(input(">>  "))
    pesq.strip()
    if pesq == "":
        menu()
        return
    else:
        with open("videos.txt", "r") as videos:
            encontrado = False
            linhas = videos.readlines()
            for linha in linhas:
                linhaS = linha.strip().split("\\")
                if linhaS[0] == pesq:
                    linhaST = linhaS
                    encontrado = True
            if encontrado:
                paginaVideo(linhaST)
                return
            else:
                print("Midia não encontrada")
                sleep(2)
                limparTerminal()
                menu()
                return

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
    global usuario
    print("Bem vindo/a, %s!" % usuario)
    print()
    print("1 - Pesquisar (por nome)")
    print("2 - Gerenciar favoritos")
    print("0 - Sair")
    print()
    print("Explorar:")
    explorar()
    inp = msvcrt.getch().decode()
    if inp == "1":
        paginaPesquisar()
        return
    elif inp == "2":
        paginaFavoritos()
        return
    elif inp == "0":
        paginaInicial()
        usuario = ""
        return
    else:
        menu()
        return

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
        return
    else:
        print()
        print("Usuário ou senha incorretos!")
        sleep(2)
        paginaInicial()
        return

def paginaSigin():
    formatarUsers()
    limparTerminal()
    print("Crie o nome de usuário:   (enter para voltar)")
    usuarior = str(input(">> "))
    usuario = usuarior.strip()
    if usuario == "":
        paginaInicial()
        return
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
            return
        else:            
            usersplit = usuario.strip().split()
            if len(usersplit) > 1:
                print("O nome de usuário não pode conter espaços!")
                sleep(2)
                paginaInicial()
                return
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
                    return
                if len(senhaa) == 0:
                    print("A senha não pode ser nula!")
                    sleep(2)
                    paginaInicial()
                    return
                else:
                    if senha1 == senha2:
                        with open("usuarios.txt" , "a") as usuarios:
                            usuarios.write("%s %s\n" % (usuario.strip(), senha1.strip()))
                        with open("favoritos.txt" , "a") as favs:
                            favs.write("%s\\\n" %usuario)
                        print("Usuário criado!")
                        sleep(1)
                        print("Você ja pode fazer login!")
                        sleep(2)
                        paginaInicial()
                        return
                    else:
                        print("As senhas não batem!")
                        sleep(2)
                        paginaInicial()
                        return

def paginaInicial():
    while True:
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
            break
        elif inp == "2":
            paginaSigin()
            break
        elif inp == "0":
            limparTerminal()
            adeus()
            break

paginaInicial()