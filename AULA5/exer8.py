somatoria = int(0)
while True:
    entrada = int(input("Digite o número a somar ou 0 para sair: "))
    if entrada == 0:
        break
    else:
        somatoria += entrada

print("Somatoria: ", somatoria)