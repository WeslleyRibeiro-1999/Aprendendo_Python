lista = [4, 10, 5, 10]

# Append - Adiciona a lista
lista.append(9)
print(lista)

# Len - Mostra a quantidade de uma lista
print(len(lista))

# Insert - Adiciona em um indice especifico
lista.insert(1, 'WESLLEY')
print(lista)

# Conta a quantidade de valores '10' tem dentro da lista
lista.count(10)

# POP - remove o ultimo item da lista
lista.pop()
# remove o elemento do indice
lista.pop(1)

# Remove - Remove o item especifico
lista.remove("weslley")

# Sort - Oderna a lista
lista.sort()
print(lista)

# Max - Retorno o maior numero de uma lista
maior = max(lista)

# Min - Retorna o menor valor de uma lista
menor = min(lista)

# Soma todos os valores da lista
soma = sum(lista)

# Index - Retorna o indice da primeira ocorrencia do que estou procurando
print(lista.index(10))

# Range
for a in range(5):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

for a in lista:
    print(a)

# in - existir em algo
if 30 in lista:
    print('O numero 30 possui na lista')
else:
    print('O numero 30 nao possui na lista')

# tuplas
tupla1 = ()
for a in range(5):
    n = input(int('Numero: '))
    tupla1 = tupla1 + (n,)
