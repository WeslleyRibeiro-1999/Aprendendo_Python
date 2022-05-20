from sqlalchemy import create_engine, Column, Integer, String, Float, desc, asc
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///sqlAlchemy/funcionario.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
session = Session()

# Instância da classe Base do SQLAlchemy
Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


arquivo = open("sqlAlchemy/123.txt", "r", encoding="UTF-8")


for a in arquivo:
    i = a.split(';')
    funcionario1 = Funcionario(i[0], int(i[1]), float(i[2]))
    session.add(funcionario1)
    session.commit()

arquivo.close()

print('-'*30)
lista_funcionario = session.query(Funcionario)
for obj in lista_funcionario:
    print(obj.id, obj.nome, obj.idade, obj.salario)

menor_salario = session.query(Funcionario).order_by(
    Funcionario.salario).first()
print('-'*30)
print(menor_salario.nome, menor_salario.salario)

mais_velhor = session.query(Funcionario).order_by(
    Funcionario.idade.desc()).first()
print('-'*30)
print(mais_velhor.nome, mais_velhor.idade)

print('-'*30)
salarios = []
media_salario = session.query(Funcionario)
for a in media_salario:
    salarios.append(a.salario)
media = sum(salarios) / len(salarios)
print("%.2f" % media)

lista_funcionario = session.query(Funcionario).order_by(Funcionario.nome.asc())
arquivo = open("sqlAlchemy/arquivo2.txt", "w", encoding="UTF-8")
for a in lista_funcionario:
    arquivo.write(a.nome + '; ')
    arquivo.write(str(a.idade) + '; ')
    arquivo.write(str(a.salario) + "\n")

arquivo.close()
connection.close()
