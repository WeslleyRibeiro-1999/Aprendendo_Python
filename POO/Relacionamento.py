'''

Exemplo de Associação de Classes:

|-------------------|           |-------------------|
| Pessoa            |           | Endereco          |
|-------------------|           |-------------------|
| nome              |           | rua               |
| idade             |-----------| numero            |
| sexo              |           | complemento       |
| endereco          |           | cep               |
|-------------------|           |-------------------|
| exibir_dados()    |           | exibir_dados()    |
|-------------------|           |-------------------|

'''


class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def exibir_dados(self):
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
        print('Sexo: ', self.sexo)
        # executa o exibir_dados da classe endereco
        self.endereco.exibir_dados()


class Endereco:
    def __init__(self, rua, numero, complemento, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep

    def exibir_dados(self):
        print('Rua: ', self.rua)
        print('Numero: ', self.numero)
        print('Complemento: ', self.complemento)
        print('Cep', self.cep)


# objeto endereco
end = Endereco('Rua Silva', 345, 'Fundos', '777777-444')

# objeto Pessoa
pessoa1 = Pessoa('Paulo', 30, 'M', end)

# objeto Pessoa
pessoa2 = Pessoa('Maria', 23, 'F', end)

# exibe os dados da pessoa
pessoa1.exibir_dados()
