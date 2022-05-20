from abc import ABC, abstractclassmethod

class Conta(ABC):
    def __init__(self, numero_conta, nome, saldo):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    @abstractclassmethod
    def deposito(self, valor):
        pass

    @abstractclassmethod
    def saque(self, valor):
        pass

    @abstractclassmethod
    def impressao_saldo(self):
        pass


class Conta_Corrente(Conta):
    def __init__(self, numero_conta, nome, saldo):
        super().__init__(numero_conta, nome, saldo)
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo < valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente para saque!')

    def impressao_saldo(self):
        print("Seu saldo é: ", self.saldo)


class Conta_Poupanca(Conta):
    def __init__(self, numero_conta, nome, saldo):
        super().__init__(numero_conta, nome, saldo)
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo < valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente para saque!')

    def impressao_saldo(self):
        print("Seu saldo é: ", self.saldo)


class Conta_Especial(Conta):
    def __init__(self, numero_conta, nome, saldo):
        super().__init__(numero_conta, nome, saldo)
        self.limite = -1000.00
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if (self.saldo - valor) >= self.limite:
            self.saldo -= valor
        else:
            print('Saldo insuficiente para saque!')

    def impressao_saldo(self):
        print("Seu saldo é: ", self.saldo)


conta1 = Conta_Corrente(1234, "Lucas", 10000.00)
conta2 = Conta_Poupanca(12345, "Sergio", 2.00)
conta3 = Conta_Especial(123456, "Weslley", -500)

conta1.saque(10000000000.00)
conta1.deposito(1000000000000000.00)
conta2.deposito(1.00)
conta2.saque(1.50)
conta3.saque(500)
conta1.impressao_saldo()
conta2.impressao_saldo()
conta3.impressao_saldo()