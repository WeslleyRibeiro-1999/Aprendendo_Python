from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///sqlAlchemy/server4.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")


class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String(255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', String(255))
    especializacao = Column('ESPECIALIZACAO', String(255))

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID_MEDICO', Integer)
    id_paciente = Column('ID_PACIENTE', Integer)
    descricao = Column('DESCRICAO', String(255))
    resultado = Column('RESULTADO', String(255))

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado


medico1 = Medico("Sergio", "0925251583", "Ginicologista")
session.add(medico1)
session.commit()

paciente1 = Paciente("Weslley", "52189723997-97", 22)
paciente2 = Paciente("Noé", "87861872248-22", 48)
lista1 = [paciente1, paciente2]
session.add_all(lista1)
session.commit()

exame1 = Exame(medico1.id, paciente1.id, "Daora", "Positivo")
exame2 = Exame(medico1.id, paciente2.id, "LEGAL", "Negativo")
lista2 = [exame1, exame2]
session.add_all(lista2)
session.commit()

print('-'*30)
resultado = session.query(Medico)             # retorna lista de objetos
for obj in resultado:
    print(obj.id, obj.nome, obj.crm, obj.especializacao)

print('-'*30)
resultado = session.query(Paciente)             # retorna lista de objetos
for obj in resultado:
    print(obj.id, obj.nome, obj.cpf, obj.idade)

print('-'*30)
resultado = session.query(Exame)             # retorna lista de objetos
for obj in resultado:
    print(obj.id, obj.id_medico, obj.id_paciente, obj.descricao, obj.resultado)
