
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///sqlAlchemy/server3.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor("Sergio")
autor2 = Autor("Weslley")

lista1 = [autor1, autor2]
session.add_all(lista1)
session.commit()

livro1 = Livro("A cabana", 120, autor1.id)
livro2 = Livro("Crepusculo", 250, autor2.id)


lista2 = [livro1, livro2]
session.commit()


session.add_all(lista2)
session.commit()

print('-'*30)
resultado = session.query(Autor)
for obj in resultado:
    print(obj.id, obj.nome)

print('-'*30)
resultado = session.query(Livro)
for obj in resultado:
    print(obj.id, obj.titulo, obj.paginas, obj.autor_id)


resultado = session.query(Livro, Autor).filter(Livro.autor_id == Autor.id)
for obj in resultado:
    print(obj.Autor.nome, obj.Livro.titulo)
