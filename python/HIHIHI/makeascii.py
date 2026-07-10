from ascii_magic import AsciiArt

# Caminho da sua imagem
imagem = ["d16514e410feb21d1a63f453c4696e2e.png", "image.png", "skibidi.jpeg" , "WhatsApp Image 2026-06-16 at 01.13.53.jpeg", "WhatsApp Image 2026-06-16 at 01.13.54.jpeg",
          "WhatsApp Image 2026-06-18 at 23.07.21.jpeg", "WhatsApp Image 2026-06-18 at 23.26.39.jpeg"]

arte = AsciiArt.from_image(imagem[6])

arte.to_terminal(columns=350)

#arte.to_file("saida.txt", columns=200)

# Se quiser salvar como imagem PNG com a arte ASCII desenhada:
# arte.to_file("saida.png", columns=200)