arquivo = open("arquivo.txt", 'w', encoding="UTF-8")
for linha in range(10):
    numero = int(input("Digite um numero: "))
    arquivo.write(str(numero) + "\n")    # \n para pular as linhas

arquivo.close()
