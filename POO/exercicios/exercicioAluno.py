class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.nota = []

    def inserir_nota(self, nota):
        if nota >= 0 <= 10:
            self.nota.append(nota)
        else:
            print('Nota invalida!')

    def calcular_media(self):
        return sum(self.nota) / len(self.nota)


nome = input('Digite seu nome: ')
ra = int(input('Digite seu RA: '))
i = 0
while len() < 4:
    i += i
    notas = float(input('Digite sua nota: '))
aluno1 = Aluno(ra, nome, 'ad2b')
aluno1.inserir_nota(notas)
