arquivo = open("arquivo.txt", "w", encoding="UTF-8")

for a in range(5):
    escreva = input("Escreva o que quiser: ")
    arquivo.write(escreva + "\n")
