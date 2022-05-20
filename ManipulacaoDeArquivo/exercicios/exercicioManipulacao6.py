arquivo = open("eu.txt", "r", encoding="UTF-8")
arquivo2 = open("eu2.txt", "r", encoding="UTF-8")
arquivo3 = open("eu3.txt", "w", encoding="UTF-8")

copia1 = arquivo.read()
copia2 = arquivo2.read()
arquivo3.write(copia1 + copia2)

lista = []
for i in copia1.split("\n"):
    lista.append(i)

print(lista)
arquivo3 = open("eu3.txt", "r", encoding="UTF-8")

copia3 = arquivo3.read()
arquivo3.close()
