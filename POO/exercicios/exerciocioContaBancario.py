class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor, senha):
        self.saldo += valor

    def sacar(self, valor, senha):
        if self.senha == senha:
            self.saldo -= valor
        else:
            print('Senha incorreta')


conta1 = ContaBancaria(1122, 'Weslley', 1234)

while True:
    senha = int(input('Digite a senha: '))
    if conta1.senha == senha:
        conta1.depositar(500, senha)
        break
    else:
        print('Senha incorreta, tente novamente!')
print('Novo saldo: ', + conta1.saldo)

conta1.sacar(200, 1234)

print('Novo saldo: ', + conta1.saldo)
