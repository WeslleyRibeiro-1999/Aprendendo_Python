class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia


class Veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    def exibir_dados(self):
        print("ano: ", self.ano)
        print("preco: ", self.preco)
        print("Cilindrada: ", self.motor.cilindrada)
        print("potencia: ", self.motor.potencia)


class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        print('\n-----------------')
        super().exibir_dados()
        print("cor: ", self.cor)
        print("modelo: ", self.modelo)


class Caminhao(Veiculo):
    def __init__(self, ano, preco, Motor, comprimento):
        super().__init__(ano, preco, Motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        print('\n-----------------')
        super().exibir_dados()
        print("comprimentos: ", self.comprimento)


motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()           # imprime os valores de todos os atributos do carro
caminhao.exibir_dados()        # imprime os valores de todos os atributos do caminhão
