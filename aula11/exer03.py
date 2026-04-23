arquivo = open("contatos.txt" , "a")
while True:
    nome = input("Digite o nome (vazio para sair): ")
    if nome == "":
        break
    telefone = input("Digite o telefone: ")
    arquivo.write("%s %s\n" % (nome,telefone))
    
arquivo.close()
arquivo = open("contatos.txt" , "r")

for i in arquivo.readlines():
    lista = i.strip().split(maxsplit=1)
    nome = lista[0]
    telefone = lista[1]  
    print("Nome: %s | Telefone: %s" % (nome,telefone))

arquivo.close()