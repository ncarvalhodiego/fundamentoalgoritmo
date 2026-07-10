"""
Snake - Jogo de terminal em Python (versao Windows, sem curses)
Use WASD para mover a cobra. Pressione 'q' para sair.

Como rodar:
    python snake.py

Feito para funcionar direto no Windows, sem instalar nada extra.
"""

import msvcrt
import os
import random
import time

LARGURA = 50
ALTURA = 30


def limpar_tela():
    os.system("cls")


def novo_jogo():
    cobra = [
        [ALTURA // 2, LARGURA // 4],
        [ALTURA // 2, LARGURA // 4 - 1],
        [ALTURA // 2, LARGURA // 4 - 2],
    ]
    direcao = "RIGHT"
    comida = gerar_comida(cobra)
    return cobra, direcao, comida


def gerar_comida(cobra):
    i = 0
    while i < 2:
        i+=1
        while True:
            pos = [random.randint(1, ALTURA - 2), random.randint(1, LARGURA - 2)]
            if pos not in cobra:
                return pos
            

def desenhar(cobra, comida, score):
    tela = [[" " for _ in range(LARGURA)] for _ in range(ALTURA)]

    # Bordas
    for x in range(LARGURA):
        tela[0][x] = "#"
        tela[ALTURA - 1][x] = "#"
    for y in range(ALTURA):
        tela[y][0] = "#"
        tela[y][LARGURA - 1] = "#"

    # Comida
    tela[comida[0]][comida[1]] = "*"

    # Cobra
    for i, (y, x) in enumerate(cobra):
        tela[y][x] = "O" if i == 0 else "o"

    limpar_tela()
    print(f" Score: {score}   (WASD para mover, Q para sair)\n")
    for linha in tela:
        print("".join(linha))


def ler_tecla(direcao_atual):
    nova = direcao_atual
    opostos = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}

    # Esvazia TODO o buffer de teclado, ficando so com a ultima tecla valida.
    # Isso evita o "delay" de comandos acumulados quando voce aperta varias
    # teclas rapido.
    while msvcrt.kbhit():
        tecla = msvcrt.getch()

        if tecla in (b"\x00", b"\xe0"):
            tecla2 = msvcrt.getch()
            mapa_setas = {
                b"H": "UP",
                b"P": "DOWN",
                b"K": "LEFT",
                b"M": "RIGHT",
            }
            candidata = mapa_setas.get(tecla2)
        else:
            mapa_wasd = {
                b"w": "UP", b"W": "UP",
                b"s": "DOWN", b"S": "DOWN",
                b"a": "LEFT", b"A": "LEFT",
                b"d": "RIGHT", b"D": "RIGHT",
                b"q": "QUIT", b"Q": "QUIT",
            }
            candidata = mapa_wasd.get(tecla)

        if candidata == "QUIT":
            return "QUIT"

        # So aceita a tecla se nao for o movimento oposto ao atual
        if candidata and opostos.get(candidata) != direcao_atual:
            nova = candidata

    return nova


def main():
    cobra, direcao, comida = novo_jogo()
    score = 0
    velocidade = 0.001  # segundos entre cada movimento

    while True:
        direcao = ler_tecla(direcao)
        if direcao == "QUIT":
            break

        cabeca = cobra[0].copy()
        if direcao == "UP":
            cabeca[0] -= 1
        elif direcao == "DOWN":
            cabeca[0] += 1
        elif direcao == "LEFT":
            cabeca[1] -= 1
        elif direcao == "RIGHT":
            cabeca[1] += 1

        # Colisao com borda ou com o proprio corpo
        if (
            cabeca[0] <= 0 or cabeca[0] >= ALTURA - 1
            or cabeca[1] <= 0 or cabeca[1] >= LARGURA - 1
            or cabeca in cobra
        ):
            break

        cobra.insert(0, cabeca)

        if cabeca == comida:
            score += 1
            comida = gerar_comida(cobra)
            if velocidade > 0.05:
                velocidade -= 0.005  # jogo vai ficando mais rapido
        else:
            cobra.pop()

        desenhar(cobra, comida, score)
        time.sleep(velocidade)

    limpar_tela()
    print(" GAME OVER ")
    print(f" Score final: {score}")
    print("\nPressione ENTER para sair...")
    input()


if __name__ == "__main__":
    main()
