from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///sqlAlchemy/server2.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")


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


funcionario1 = Funcionario("Sergio", 21, 2500.00)
funcionario2 = Funcionario("Weslley", 22, 3500.50)
funcionario3 = Funcionario("Luana", 17, 600.00)
lista = [funcionario1, funcionario2, funcionario3]
session.add_all(lista)
session.commit()

print('-'*30)
resultado = session.query(Funcionario)
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)

print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)
