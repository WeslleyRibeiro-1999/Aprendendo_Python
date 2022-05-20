class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        print('-'*30)
        print("Nome: " + self.nome)
        print("Email: " + self.email)
        print("Telefone: " + self.telefone)


lista = []

while True:
    nome = input("Informe o nome: ")
    if nome == "":
        break
    email = input("Informe seu email: ")
    telefone = input("Informe seu telefone: ")
    pessoa1 = Pessoa(nome, email, telefone)
    lista.append(pessoa1)

for p in lista:
    p.exibir_dados()
