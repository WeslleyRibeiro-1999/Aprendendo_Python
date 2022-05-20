class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado
    
    def imprimir_exame(self):
        print('Solicitante: ', self.medico.nome + ', ', self.medico.crm)
        print('Paciente: ', self.paciente.nome + ', ' + self.paciente.cpf)
        if self.descricao == 'COVID-19':
            if self.resultado == "Positivo":
                print('O auto-teste de COVID-19 deu como resultado: ', self.resultado)
            else:
                print('O auto-teste de COVID-19 deu como resultado: ', self.resultado)


paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)
