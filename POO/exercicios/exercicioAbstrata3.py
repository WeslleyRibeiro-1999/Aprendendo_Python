from abc import ABC, abstractclassmethod


class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractclassmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base * self.salario_base


class Assistente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.10)


get = Gerente("Lucas", 2104568, 1000.00)
assis = Assistente("Sergio", 2058796, 1000.00)
vend = Vendedor("Weslley", 2356894, 1000.00)
print('Print:  ', vend.calcular_salario())
lista = [get, assis, vend]

for a in lista:
    print("Salario do " + a.nome + " é: ", a.calcular_salario())
