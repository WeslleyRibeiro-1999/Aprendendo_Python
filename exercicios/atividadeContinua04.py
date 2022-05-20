# ALUNO 1: Weslley Ribeiro da Silva
# ALUNO 2: Sergio Yuri Dias Soares
# ALUNO 3: Isabella Braga Medeiros Passos
# ALUNO 4: Lucas Henrique Guede Lopes


from abc import ABC, abstractclassmethod


class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @abstractclassmethod
    def mostrar_informacoes(self):
        print('Nome: ', self.nome)
        print('CPF: ', self.cpf)
        print('Telefone: ', self.telefone)


class Clinica():
    def __init__(self):
        self.medicos = []
        self.pacientes = []

    def adicionar_medicos(self, medico):
        self.medicos.append(medico)

    def adicionar_pacientes(self, paciente):
        self.pacientes.append(paciente)


class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, crm, salario):
        super().__init__(nome, cpf, telefone)
        self.crm = crm
        self.especialidades = []
        self.salario = salario
        self.exerce = None

    def adicionar_especialidade(self, especialidades):
        self.especialidades.append(especialidades)

    def especialidade_exercida(self, especialidade):
        for a in self.especialidades:
            if a == especialidade:
                self.exerce = especialidade

    def mostrar_informacoes(self):
        print('Nome: ', self.nome)
        print('CPF: ', self.crm)
        print('Telefone: ', self.salario)


class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, endereco, data_nascimento,
                 medico, quarto):
        super().__init__(nome, cpf, telefone)
        self.__rg = rg
        self.__endereco = endereco
        self.dataNascimento = data_nascimento
        self.medico = medico
        self.quarto = quarto
        self.visitas = []

    def adicionar_visita(self, visita):
        if visita.quarto == self.quarto:
            self.visitas.append(visita)
        else:
            print('Paciente e quarto não condizem com o registro do sistema.')

    def get_rg(self):
        return self.__rg

    def get_endereco(self):
        return self.__endereco

    def mostrar_informacoes(self):
        print('Nome: ', self.nome)
        print('Data de Nascimento: ', self.dataNascimento)
        print('Medico: ', self.medico.nome)


class Quarto:
    def __init__(self, numero, andar):
        self.numero = numero
        self.andar = andar


class Visitas:
    def __init__(self, data, quarto, registro, medico):
        self.data = data
        self.quarto = quarto
        self.registro = registro
        self.medico = medico
