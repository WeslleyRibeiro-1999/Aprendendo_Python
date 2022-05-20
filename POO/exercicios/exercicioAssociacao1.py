class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, meucarro):
        self.carro = meucarro


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('Weslley', 22)

eu.comprar_carro(meucarro)

print('Meu nome: ', eu.nome)
print('Modelo do meu carro: ', eu.carro.modelo)
print('Placa do meu carro: ', eu.carro.placa)