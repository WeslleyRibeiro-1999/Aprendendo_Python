arquivo = open("arquivo.txt", "r", encoding="UTF-8")

resultado = 0
for linha in arquivo:
    resultado += int(linha)

print(resultado)

arquivo.close()
