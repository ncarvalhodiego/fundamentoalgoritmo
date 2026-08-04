import time, math
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from PIL import Image, ImageTk

# todas as barras tem esse tamanho, nao importa o maximo de cada stat
LARGURABARRA = 170
LARGURABARRAAURA = 260
ALTURABARRA = 18
ALTURABARRAAURA = 24

SEMLIMITE = 99999999

# lugares de cada regiao, com o x e o y de cada botao na mao pra ficarem desalinhados
LUGARES = {
    "Santo André": [
        ("Bosque", 30, 95),
        ("Inhel", 200, 140),
        ("Mineiro", 370, 100),
        ("Beco Figueiras", 525, 150),
        ("Gold", 50, 225),
        ("868", 215, 270),
        ("Pagodinho", 385, 220),
        ("Adega Jardim", 540, 275),
        ("Diego", 285, 325),
    ],
    "São Bernardo": [
        ("Academia", 35, 100),
        ("Beco Kennedy", 205, 145),
        ("Supra Berno", 375, 95),
        ("Sonda", 535, 150),
        ("Supra Direito", 60, 230),
        ("Padaria Kennedy", 240, 270),
        ("Datamaxi", 420, 225),
    ],
    "São Caetano": [
        ("Goais", 60, 120),
        ("Liv", 260, 190),
        ("Duplex", 460, 130),
    ],
}

TITULO = "Servilla Simulator®"

# o jaoas perde 5 de saciedade a cada 20 segundos
INTERVALOFOME = 20000
PERDAFOME = 5

# de barriga vazia ele cansa 10 a cada 5 segundos
INTERVALOCANSACO = 5000
CANSACODAFOME = 10

PERDASACIEDADEDORMIR = 20

TAMANHOFOTO = 100
fotoperfil = None

# janelas abertas no momento
janela2 = None      # mapa
janela3 = None      # regiao
janela4 = None      # lugar
janelacasa = None
painel = None       # quadro dos stats na tela principal

# zera toda vez que o jaoas dorme
usosdodia = {"pc": 0, "tv": 0, "resenha": 0}


# valor que enche a barra de cada stat, aura e conhecimento dependem das flags do save
def calcularMaximos(save):
    return {
        "Aura": 5000 if save.get("limitaraura") else SEMLIMITE,
        "Saciedade": 100,
        "Tesao": 100,
        "Conhecimento": 100 if save.get("limitarconhecimento") else SEMLIMITE,
        "Cansaco": 100,
    }


def carregarSave(arquivo="saveplayer.txt"):
    save = {}
    with open(arquivo, "r", encoding="utf-8") as a:
        for linha in a:
            linha = linha.strip()
            if "=" not in linha:
                continue
            chave, valor = linha.split("=", 1)
            if valor == "True" or valor == "False":
                save[chave] = valor == "True"
            else:
                try:
                    save[chave] = int(valor)
                except ValueError:
                    save[chave] = valor
    return save


def gravarSave(arquivo="saveplayer.txt"):
    # sem quebra de linha no final pra ficar igualzinho ao savezerado.txt,
    # senao o main.py nunca mais reconhece um jogo novo
    linhas = [f"{chave}={valor}" for chave, valor in save.items()]
    with open(arquivo, "w", encoding="utf-8") as a:
        a.write("\n".join(linhas))


def criarBarra(pai, texto, valor, maximo, cor, linha, largura=LARGURABARRA, altura=ALTURABARRA, mostrarvalor=False):
    rotulo = tk.Label(pai, text=texto, font=("Arial", 12, "bold"), width=12, anchor="w")
    rotulo.grid(row=linha, column=0, sticky="w", pady=4)

    barra = tk.Canvas(pai, width=largura, height=altura, bg="#d9d9d9",
                      highlightthickness=1, highlightbackground="black")
    barra.grid(row=linha, column=1, sticky="w", pady=4)

    cheio = min(max(valor, 0), maximo) / maximo * largura
    if cheio > 0:
        barra.create_rectangle(0, 0, cheio, altura, fill=cor, width=0)

    # so aparece enquanto o mouse esta em cima da barra
    if mostrarvalor:
        valorbarra = tk.Label(pai, text="", font=("Arial", 16, "bold"), fg="#776e0c", width=12, anchor="w")
        valorbarra.grid(row=linha, column=2, padx=(8,0), sticky="w")
        barra.bind("<Enter>", lambda evento: valorbarra.config(text=f"{valor}"))
        barra.bind("<Leave>", lambda evento: valorbarra.config(text=""))

    return barra


def criarBotao(texto, funcao, x, y):
    botao = tk.Button(janela, command=funcao, text=texto, width=10, height=3, font=("Arial", 14, "bold"))
    botao.pack()
    botao.place(x=x, y=y)


def carregarFotoPerfil():
    # guarda numa global pra nao reabrir o jpeg toda vez que o painel é refeito,
    # e tambem pra imagem nao sumir com o coletor de lixo do python
    global fotoperfil

    if fotoperfil is None:
        imagem = Image.open("emojinerd.jpg").resize((TAMANHOFOTO, TAMANHOFOTO))
        fotoperfil = ImageTk.PhotoImage(imagem)

    return fotoperfil


def montarPainel():
    global painel

    # o painel inteiro é refeito do zero toda vez que algum stat muda
    fecharjanela(painel)

    painel = tk.Frame(janela)
    painel.place(x=20, y=80)

    stats = tk.Label(painel, text="   Jaoas Stats", font=("Arial", 16, "bold"))
    stats.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,10))

    # sobe de 1 em 1 cada vez que o jaoas dormir
    dia = tk.Label(painel, text=f"Dia {save['Dia']}", font=("Arial", 14, "bold"))
    dia.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0,8))

    # foto do player + dinheiro do lado
    linhafoto = tk.Frame(painel)
    linhafoto.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0,10))

    fotoplayer = tk.Canvas(linhafoto, width=TAMANHOFOTO, height=TAMANHOFOTO, bg="white",
                           highlightthickness=2, highlightbackground="black")
    fotoplayer.pack(side="left")
    fotoplayer.create_image(0, 0, image=carregarFotoPerfil(), anchor="nw")

    dinheiro = tk.Label(linhafoto, text=f"R$ {save['Dinheiro']}", font=("Arial", 16, "bold"), fg="#1a7a1a")
    dinheiro.pack(side="left", padx=15)

    maximos = calcularMaximos(save)

    criarBarra(painel, "Aura", save["Aura"], maximos["Aura"], "#c9ba15", 3,
               largura=LARGURABARRAAURA, altura=ALTURABARRAAURA, mostrarvalor=True)
    criarBarra(painel, "Saciedade", save["Saciedade"], maximos["Saciedade"], "#2ecc40", 4)
    criarBarra(painel, "Tesão", save["Tesao"], maximos["Tesao"], "#e02020", 5)
    criarBarra(painel, "Conhecimento", save["Conhecimento"], maximos["Conhecimento"], "#2060e0", 6)
    criarBarra(painel, "Cansaço", save["Cansaco"], maximos["Cansaco"], "#000000", 7)

    rotulocomida = tk.Label(painel, text="Comida", font=("Arial", 12, "bold"), width=12, anchor="w")
    rotulocomida.grid(row=8, column=0, sticky="w", pady=4)
    comida = tk.Label(painel, text=f"{save['Comida']} un.", font=("Arial", 12, "bold"))
    comida.grid(row=8, column=1, sticky="w", pady=4)


def passarFome():
    save["Saciedade"] = max(save["Saciedade"] - PERDAFOME, 0)
    montarPainel()
    janela.after(INTERVALOFOME, passarFome)


def cansarDeFome():
    # so mexe no painel quando a barriga esta vazia mesmo
    if save["Saciedade"] <= 0:
        save["Cansaco"] = min(save["Cansaco"] + CANSACODAFOME, calcularMaximos(save)["Cansaco"])
        montarPainel()

    janela.after(INTERVALOCANSACO, cansarDeFome)


def telaMain():
    global janela, save, botaomapa, botaocasa
    janela = tk.Tk()
    janela.title(TITULO)
    janela.geometry("700x500+30+30")

    save = carregarSave()

    titulo = tk.Label(text="   Jaoas Life   ", font=("Arial", 20, "bold"))
    titulo.pack(pady=(20,20))

    montarPainel()

    botaocasa = tk.Button(janela, command=telaCasa, text="CASA", width=10, height=3, font=("Arial", 14, "bold"))
    botaocasa.place(x=550, y=310)

    botaomapa = tk.Button(janela, command=telaMapa, text="MAPA", width=10, height=3, font=("Arial", 14, "bold"))
    botaomapa.place(x=550, y=400)

    janela.after(INTERVALOFOME, passarFome)
    janela.after(INTERVALOCANSACO, cansarDeFome)

    janela.protocol("WM_DELETE_WINDOW", fecharjogo)


def fecharjogo():
    gravarSave()
    janela.destroy()


def fecharjanela(alvo):
    if alvo is not None and alvo.winfo_exists():
        alvo.destroy()


def fecharmapa():
    # fechar o mapa fecha a regiao e o lugar que estiverem abertos
    fecharjanela(janela3)
    fecharjanela(janela4)
    fecharjanela(janela2)
    botaomapa.place(x=550, y=400)


def fecharcasa():
    fecharjanela(janelacasa)
    botaocasa.place(x=550, y=310)


def telaMapa():
    global janela2

    # casa e mapa nunca ficam abertos ao mesmo tempo
    fecharcasa()

    botaomapa.place_forget()
    janela2 = tk.Toplevel(janela)
    janela2.title(TITULO)
    janela2.geometry("280x360+750+60")

    titulo = tk.Label(janela2, text=("MAPA"), font=("Arial", 20, "bold"))
    titulo.pack(pady=(20,20))

    # regioes
    regioes = ["Santo André", "São Bernardo", "São Caetano"]
    for regiao in regioes:
        botao = tk.Button(janela2, text=regiao, width=14, height=2, font=("Arial", 12, "bold"),
                          command=lambda r=regiao: telaRegiao(r))
        botao.pack(pady=10)

    janela2.protocol("WM_DELETE_WINDOW", fecharmapa)


def telaRegiao(nome):
    global janela3

    # so deixa uma regiao aberta por vez pra nao encher a tela de janelas
    fecharjanela(janela3)

    # trocar de regiao tira o jaoas do lugar onde ele estava
    fecharjanela(janela4)

    janela3 = tk.Toplevel(janela)
    janela3.title(f"Servilla Simulator® - {nome}")
    janela3.geometry("700x400+750+520")

    titulo = tk.Label(janela3, text=nome, font=("Arial", 20, "bold"))
    titulo.pack(pady=(20,20))

    # lugares da regiao
    for lugar, x, y in LUGARES[nome]:
        botao = tk.Button(janela3, text=lugar, width=15, height=2, font=("Arial", 11, "bold"),
                          command=lambda l=lugar: telaLugar(l, nome))
        botao.place(x=x, y=y)


def telaLugar(nome, regiao):
    global janela4

    # entrar no lugar fecha o mapa da regiao
    fecharjanela(janela3)

    janela4 = tk.Toplevel(janela)
    janela4.title(f"Servilla Simulator® - {nome}")
    janela4.geometry("500x350+850+560")

    titulo = tk.Label(janela4, text=nome, font=("Arial", 20, "bold"))
    titulo.pack(pady=(20,20))

    # coisas pra fazer no lugar

    # sair do lugar traz a regiao de volta
    def fecharlugar():
        janela4.destroy()
        telaRegiao(regiao)

    janela4.protocol("WM_DELETE_WINDOW", fecharlugar)


def acaoDormir():
    save["Dia"] += 1
    save["Cansaco"] = 0
    save["Saciedade"] = max(save["Saciedade"] - PERDASACIEDADEDORMIR, 0)

    for chave in usosdodia:
        usosdodia[chave] = 0

    montarPainel()
    messagebox.showinfo(TITULO, "Você dormiu gostosinho...")


def acaoComer():
    if save["Comida"] < 1:
        messagebox.showerror(TITULO, "Você não tem comida fdp")
        return

    save["Comida"] -= 1
    save["Saciedade"] = min(save["Saciedade"] + 13, calcularMaximos(save)["Saciedade"])

    montarPainel()
    messagebox.showinfo(TITULO, "Você comeu um pão com miojão e cocô (brincadeira rs)")


def acaoJogar():
    if usosdodia["pc"] >= 2:
        messagebox.showerror(TITULO, "Você ja jogou demais veyyryyrrrrrrr")
        return

    usosdodia["pc"] += 1
    save["Tesao"] = min(save["Tesao"] + 4, calcularMaximos(save)["Tesao"])
    save["Cansaco"] = max(save["Cansaco"] - 10, 0)

    montarPainel()
    messagebox.showinfo(TITULO, "Você jogou topzera com os bro, ficou bem chilling e relaxou")


def acaoEstudar():
    maximos = calcularMaximos(save)

    # estudar cansa, entao nao rola se os 15 de cansaco nao couberem
    if save["Cansaco"] + 15 > maximos["Cansaco"]:
        messagebox.showerror(TITULO, "Você esta muito cansado lil bro")
        return

    save["Cansaco"] += 15
    save["Conhecimento"] = min(save["Conhecimento"] + 5, maximos["Conhecimento"])

    montarPainel()
    messagebox.showinfo(TITULO, "Você estudou calculos insanos e infames de engenharia e deixou seu cerebro mais fodão")


def acaoVerTV():
    if usosdodia["tv"] >= 1:
        messagebox.showerror(TITULO, "Seu pai te chamou de vagabundo e falou para sair do sofa e ir fazer alguma coisa da vida")
        return

    usosdodia["tv"] += 1
    save["Cansaco"] = max(save["Cansaco"] - 7, 0)

    montarPainel()
    messagebox.showinfo(TITULO, "Você viu TV com os seus pais bem big chilling e ficou dboa")


def acaoResenhar():
    usosdodia["resenha"] += 1

    # como o contador so zera dormindo, a quarta resenha acontece uma vez por dia
    if usosdodia["resenha"] == 4:
        save["Cansaco"] = 0
        montarPainel()
        messagebox.showinfo(TITULO, "Você gozou nas calças de tanta resenha")
        return

    messagebox.showinfo(TITULO, "Você resenhou bastante RESENGAAAAAAAAN")


def telaCasa():
    global janelacasa

    # casa e mapa nunca ficam abertos ao mesmo tempo
    fecharmapa()

    botaocasa.place_forget()
    janelacasa = tk.Toplevel(janela)
    janelacasa.title(f"{TITULO} - Casa")
    janelacasa.geometry("320x480+750+60")

    titulo = tk.Label(janelacasa, text="CASA", font=("Arial", 20, "bold"))
    titulo.pack(pady=(20,15))

    # o terceiro item é o textinho que aparece do lado do botao
    acoes = [
        ("Dormir", acaoDormir, ""),
        ("Comer comida", acaoComer, "-1 comida"),
        ("Jogar no pc", acaoJogar, ""),
        ("Estudar", acaoEstudar, ""),
        ("Ver TV", acaoVerTV, ""),
        ("Resenhar com os pais", acaoResenhar, ""),
    ]

    # grid pra os botoes ficarem alinhados mesmo com o texto do lado
    quadro = tk.Frame(janelacasa)
    quadro.pack()

    for i, (texto, funcao, custo) in enumerate(acoes):
        botao = tk.Button(quadro, text=texto, width=22, height=2, font=("Arial", 11, "bold"), command=funcao)
        botao.grid(row=i, column=0, pady=5)

        if custo:
            aviso = tk.Label(quadro, text=custo, font=("Arial", 8))
            aviso.grid(row=i, column=1, padx=(6,0), sticky="w")

    janelacasa.protocol("WM_DELETE_WINDOW", fecharcasa)