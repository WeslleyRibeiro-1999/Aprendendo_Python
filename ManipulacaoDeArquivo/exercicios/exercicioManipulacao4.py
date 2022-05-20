arquivo = open("arquivo.txt", "r", encoding="UTF-8")

vogais = 0

v = arquivo.read()


for a in v:
    if a.lower() in "aeiou":
        vogais += 1

print(vogais)
