class Cachorro:
    # atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.Idade = idade

    # metodos
    def andar(self, distancia):
        print("O cachorro andou " + str(distancia) + " metros")

    def comer(self):
        print(self.nome + ' comeu')

    def latir(self):
        print("Au, Au... ")


dog = Cachorro('rex', 5)
dog.andar(5)
dog.comer()
dog.latir()
dog.nome = "Pandora"
dog.Idade = 4

print(dog.nome)
