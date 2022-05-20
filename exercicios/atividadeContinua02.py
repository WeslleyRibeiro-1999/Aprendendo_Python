# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Weslley Ribeiro da Silva
# ALUNO 2: Sergio Yuri Dias Soares
# ALUNO 3: Isabella Braga Medeiros Passos
# ALUNO 4: Lucas Henrique Guede Lopes
# ALUNO 5:
# ALUNO 6:


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = 147.00
        self.__valor_fixo_letra = 0.35
        self.__valor_total = None

    def get_valor_total(self):
        area = self.altura * self.largura
        custo_material = area * self.__valor_fixo_material
        custo_desenho = len(self.frase.replace(" ", "")) * \
            self.__valor_fixo_letra
        self.__valor_total = custo_material + custo_desenho
        return self.__valor_total


class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def calcular_faturamento(self):
        total = 0
        for p in self.__pedidos:
            total += p.get_valor_total()
        return total
