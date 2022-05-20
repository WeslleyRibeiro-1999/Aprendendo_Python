'''
Nome da classe
    Carro
Atributos:
    marca
    modelo
    placa
Métodos:
    __init__(self, marca, modelo, placa)
    exibir_dados(self)

No programa principal, crie dois objetos da classe Carro.
Utilize o método exibir_dados para exibir os atributos de cada carro.
'''


class Carro:
    # construtor
    def __init__(self, marca, modelo, placa):
        # atributo
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print('--------------------------------')
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Placa: ', self.placa)


# lista de objetos da classe Carro
lista = []

# cadastra varios carros
while True:
    marca = input('Marca do carro (Digite SAIR para finalizar): ')
    if marca == 'SAIR':
        break
    modelo = input('Modelo do Carro: ')
    placa = input('Placa do Carro: ')

    carro1 = Carro(marca, modelo, placa)        # cria um objeto
    lista.append(carro1)                        # insere objeto na lista

# percorre lista de objeto
for carro in lista:
    carro.exibir_dados()                    # exibe informação de cada carro
