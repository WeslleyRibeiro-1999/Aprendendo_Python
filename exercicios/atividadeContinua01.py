# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Weslley Ribeiro - RA: 2102565
# ALUNO 2: Sergio Yuri - RA: 1902727
# ALUNO 3: Isabela Passos - RA: 2100518
# ALUNO 4: Lucas dos Santos - RA: 2102828
# ALUNO 5: nome
# ALUNO 6: nome


'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e dois itens e retorna True, se os dois itens estiverem
armazenado na lista, e False, caso contrário.
'''


def pertence(lista, item1, item2):
    if item1 in lista and item2 in lista:
        return True
    else:
        return False


'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma lista e dois itens (velho e novo) e retorna uma lista onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    for i, item in enumerate(lista):
        if item == velho:
            lista[i] = novo
    return lista


'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item):
    a = []
    for i, b in enumerate(tupla):
        if item == b:
            a.append(i)
    return a


'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'reprovados' que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
'''


def reprovados(alunos):
    lista = []
    for a in alunos:
        media = sum(alunos[a]) / len(alunos[a])
        if media < 6:
            lista.append(a)
    return lista


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de
entrada o dicionário e o nome de um aluno. A função deve excluir a primeira
nota desse aluno e retornar o dicionário com as alterações realizadas.
Se o aluno não existir no dicionário, deve retornar o dicionário sem alterações
'''


def excluir_nota(alunos, nome):
    if nome in alunos:
        del alunos[nome][0]
    return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maior_nota que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a maior nota
de cada aluno.
'''


def maior_nota(alunos):
    maior = {}
    for a in alunos:
        maior[a] = max(alunos[a])
    return maior
