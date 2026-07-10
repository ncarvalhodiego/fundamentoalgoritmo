import msvcrt

while True:
    tecla = msvcrt.getch()

    # Verifica se é uma tecla especial
    if tecla in (b'\x00', b'\xe0'):
        tecla = msvcrt.getch()

        if tecla == b'H':
            print("↑ Cima")
        elif tecla == b'P':
            print("↓ Baixo")
        elif tecla == b'K':
            print("← Esquerda")
        elif tecla == b'M':
            print("→ Direita")
            
    else:
        if tecla == b'q':
            break