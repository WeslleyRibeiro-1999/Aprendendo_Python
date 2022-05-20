arquivo = open("arquivo01.txt", "r", encoding="UTF-8")


ano = int(input('Digite o ano atual: '))
for i in arquivo:
    lista = i.split(' ')
    nascimento = ano - int(lista[-1])
    print(lista[0] + ' ' + str(nascimento))
