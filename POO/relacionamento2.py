'''
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| nome       |0..*    1| cliente             |1      1| nome        |
| preco      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produto()    |
                       | calcular_total()    |
                       |---------------------|
'''


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

    def calcular_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.preco
        print('Total: ', soma)


cliente1 = Cliente('Paulo')

produto1 = Produto('Pen Drive', 30)
produto2 = Produto('Celular', 1200)
produto3 = Produto('HD Externo', 120)

carrinho1 = Carrinho(cliente1)
carrinho1.inserir_produto(produto1)
carrinho1.inserir_produto(produto1)
carrinho1.inserir_produto(produto2)

carrinho1.listar_produto()
carrinho1.calcular_total()
