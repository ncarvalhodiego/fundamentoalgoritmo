from funcoessec import limparTerminal, adeus
import msvcrt, time

def adicionarTarefa():
    limparTerminal()
    with open("tarefas.txt", "r") as arquivotarefas:
        linhas = []
        for i in arquivotarefas:
            linhas.append("%s"%i)
    print("De um nome à tarefa:   (espaço para voltar)")
    x = input(str(">> "))
    x = x.strip()
    if x != "":
        with open("tarefas.txt", "w") as arquivotarefas:
            linhas.append("%s$aberta\n"%x)
            arquivotarefas.writelines(linhas)
        limparTerminal()
        print("Adicionado com sucesso!")
        time.sleep(0.7)
    menu()
    return

def printTarefas(comnumero = False, delay = 0):
    with open("tarefas.txt", "r") as arquivotarefas:
        print()
        n = 0
        for i in arquivotarefas:
            time.sleep(delay)
            n+=1
            i = i.strip().split("$")
            if comnumero:
                if i[1] == "aberta":
                    print("%d - [ ] %s" % ((n),i[0]))
                    print()
                elif i[1] == "feito":
                    print("%d - [✓] %s" % ((n),i[0]))
                    print()
            else:
                if i[1] == "aberta":
                    print("[ ] " + i[0])
                    print()
                elif i[1] == "feito":
                    print("[✓] " + i[0])
                    print()
        if n == 0:
            print()
            print("Não há tarefas por enquanto...")

def removerTarefas():
    with open("tarefas.txt", "r") as arquivortarefas:
        limparTerminal()
        printTarefas(True)
        print()
        print("Número da tarefa que será removida: (LIMPAR para excluir todas)")
        try:
            inp = input(">> ")
            x = int(inp)
        except:
            if inp.lower() == "limpar":
                with open("tarefas.txt", "w") as a:
                    a.write("")
            menu()
            return
        lista = []
        situacao = []
        for i in arquivortarefas:
            i = i.strip().split("$")
            situacao.append(i[1])
            lista.append(i[0])
        if x <= (len(lista))+1:
            lista.pop(x-1)
            situacao.pop(x-1)
            with open("tarefas.txt", "w") as arquivotarefas:
                for i in range(len(lista)):
                    arquivotarefas.writelines("%s$%s\n"%(lista[i],situacao[i]))
            limparTerminal()
            print("Removido com sucesso!")
            time.sleep(0.7)
        else:
            limparTerminal()
            print("Não foi possível encontrar a tarefa")
            time.sleep(2)
    menu()
    return

def marcarTarefa():
    limparTerminal()
    printTarefas(True)
    print()
    print("Número da tarefa:")
    try:
        inp = input(">> ")
        x = int(inp)
    except:
        menu()
        return
    with open("tarefas.txt", "r") as arquivotarefas:
        linhas = []
        n = 0
        for i in arquivotarefas:
            n+=1
            if n != int(x):
                linhas.append(i)
            else:
                linha = i.strip().split("$")
                print(linha)
                if linha[1] == "aberta":
                    linhas.append("%s$feito\n" %(linha[0]))
                elif linha[1] == "feito":
                    linhas.append("%s$aberta\n" %(linha[0]))
        if x > n or x <= 0:
            limparTerminal()
            print("Digite um número disponível")
            time.sleep(1)
    with open("tarefas.txt", "w") as arquivotarefas:
        arquivotarefas.writelines(linhas)
    menu()
    return

def menu(delay = 0):
    limparTerminal()
    print("TAREFAS")
    time.sleep(delay)
    print()
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Alternar tarefa concluída")
    print("4 - Sair")
#    time.sleep(delay)
    if delay == 0:
        printTarefas()
    else:
        printTarefas(False, 0.05)
    try:
        inp = msvcrt.getch().decode()
    except UnicodeDecodeError:
        menu()
        return
    if inp == "1":
        adicionarTarefa()
        return
    elif inp == "2":
        removerTarefas()
        return
    elif inp == "3":
        marcarTarefa()
        return
    elif inp == "4" or inp == "5" or inp == "6" or inp == "7" or inp == "8" or inp == "9" or inp == "0":
        adeus()
        return
    else:
        menu()
        return

menu(0.2)