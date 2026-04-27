import os
import platform
import time

def limparterminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    print("1 - Novo contato")
    print("2 - Procura (pelo nome)")
    print("3 - Atualiza contato")
    print("4 - Apaga contato")
    print("0 - Sair")

while True:
    limparterminal()
    menu()
    inp = int(input(""))

    if inp == 0:
        limparterminal()
        break
    elif inp == 1:
        with open("agenda.txt", "a") as agenda:
            limparterminal()
            nome = str(input("Digite o nome: "))
            numero = str(input("Digite o telefone: "))
            registrar = str("\n%s %s" % (nome,numero))
            agenda.write(registrar)
            print("Registrado!...")
            time.sleep(0.5)
            limparterminal()
    elif inp == 2:
        with open("agenda.txt", "r") as agenda:
            limparterminal()
            nome = str(input("Digite o nome desejado: "))
            for linha in agenda.readlines():
                linhaa = linha.strip().split(maxsplit=1)
                print()
                if str(linhaa[0]) == nome:
                    print("Nome: %s | Telefone: %s\n" % (str(linhaa[0]), str(linhaa[1])))
                    input("Enter para sair")
                    limparterminal()
                    break
    elif inp == 3:
        with open("agenda.txt", "r") as agenda:
            limparterminal()
            linhas = agenda.readlines()
            atualizado = False
            nome = str(input("Digite o contato a ser atualizado: "))
            novaslinhas = []

            for linha in linhas:
                linhasplit = linha.strip().split(maxsplit=1)
                if linhasplit[0] == nome:
                    novonum = str(input("Digite o novo número: "))
                    novaslinhas.append("%s %s\n" % (nome,novonum))
                    atualizado = True
                else:
                    novaslinhas.append(linha)
        with open("agenda.txt", "w") as agenda:
            agenda.writelines(novaslinhas)
        if atualizado:
            print("Contato atualizado!")
        else:
            print("Erro ao encontrar o contato")
    elif inp == 4:
        with open("agenda.txt", "r") as agenda:
            limparterminal()
            deletado = False
            linhas = agenda.readlines()
            nome = str(input("Digite o contato a ser deletado: "))
            novaslinhas = []
            for linha in linhas:
                linhasplit = linha.strip().split(maxsplit=1)
                if linhasplit[0] != nome:
                    novaslinhas.append(linha)
                else:
                    deletado = True
        with open("agenda.txt", "w") as agenda:
            agenda.writelines(novaslinhas)
    else:
        print("Opção Inválida")
        time.sleep(1)
        limparterminal()