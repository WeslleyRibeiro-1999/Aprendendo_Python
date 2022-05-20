class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero
    
    def get_titulo(self):
        return self.__titulo
    
    def get_genero(self):
        return self.__genero
        
    def set_titulo(self, novo):
        self.__titulo = novo

    def set_genero(self, novo):
        self.__genero = novo
     

filme1 = Filme("Bee-Movie", "Infantil")
filme2 = Filme("Velozes e furiosos", "Ação")
filme3 = Filme("Avatar", "Aventura")

filmes = []

filmes.append(filme1)
filmes.append(filme2)
filmes.append(filme3)

for a in filmes:
    print("Filme: ", a.get_titulo())
    print("Genero: ", a.get_genero())
