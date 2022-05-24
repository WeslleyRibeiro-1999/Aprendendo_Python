# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# ALUNO 1: Weslley Ribeiro da Silva
# ALUNO 2: Sergio Yuri Dias Soares
# ALUNO 3: Isabella Braga Medeiros Passos
# ALUNO 4: Lucas Henrique Guede Lopes
# ALUNO 5: nome
# ALUNO 6: nome

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float, asc
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

# Cria a tabela FILME no banco de dados
connection.execute('''CREATE TABLE IF NOT EXISTS FILME(
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255),
                        ANO INT,
                        DURACAO INT,
                        PAIS VARCHAR(255),
                        DIRETOR VARCHAR(255),
                        AVALIACAO FLOAT)''')


# Implementar classe Filme e realizar o mapeamento da tabela
class Filme(Base):
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    ano = Column('ANO', Integer)
    duracao = Column('DURACAO', Integer)
    pais = Column('PAIS', String(255))
    diretor = Column('DIRETOR', String(255))
    avaliacao = Column('AVALIACAO', Float)

    def __init__(self, titulo, ano, duracao, pais, diretor, avaliacao):
        self.titulo = titulo
        self.ano = ano
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.avaliacao = avaliacao


# Importar filmes do arquivo movies.txt e inserir no banco de dados
arquivo = open("movies.txt", "r", encoding="UTF-8")

for a in arquivo:
    i = a.split(';')
    filme1 = Filme(i[0], int(i[1]), int(i[2]), i[3], i[4], float(i[5]))
    session.add(filme1)
    session.commit()
arquivo.close()

# Consultar todos os filmes e ordenar pelo título
lista_filme = session.query(Filme).order_by(Filme.titulo)

# Consultar filmes do ano de 2020 e ordenar pelo título
lista_2020 = session.query(Filme).filter(
    Filme.ano == 2020).order_by(Filme.titulo)

# Consultar filmes de 2019 com avaliação superior a 80 e ordenar pelo título
lista_2019 = session.query(Filme).filter(
    Filme.ano == 2019, Filme.avaliacao > 80.00).order_by(Filme.titulo)

# Excluir todos os filmes do ano de 2020
excluir_2020 = session.query(Filme).filter(Filme.ano == 2020).delete()

# Exportar filmes para um arquivo de texto, ordenados pelo título e no formato:
# título;ano;duracao;país;diretor;avaliacao
lista_ordernada = session.query(Filme).order_by(Filme.titulo.asc())
arquivo = open("movies2020.txt", "w", encoding="UTF-8")
for a in lista_ordernada:
    arquivo.write(a.titulo + ';')
    arquivo.write(str(a.ano) + ';')
    arquivo.write(str(a.duracao) + ';')
    arquivo.write(a.pais + ';')
    arquivo.write(a.diretor + ';')
    arquivo.write(str(a.avaliacao) + '\n')
arquivo.close()
