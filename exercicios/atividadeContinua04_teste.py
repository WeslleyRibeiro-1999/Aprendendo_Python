from ac04 import Medico, Quarto, Paciente, Visitas, Clinica


try:
    # Criação da classe Medico
    olavo = Medico('Olavo R.', '21321331-12', 1193323422, '1234-5', 22300.00)
    assert olavo.nome == 'Olavo R.'
    assert olavo.cpf == '21321331-12'
    assert olavo.telefone == 1193323422
    assert olavo.crm == '1234-5'
    assert olavo.salario == 22300.00
    print('CORRETO: Criação do objeto Medico')
except Exception:
    print('ERRO...: Criação do objeto Medico')


try:
    # Criação especialidades Medico
    olavo.adicionar_especialidade('Urologista')
    olavo.adicionar_especialidade('Ortopedia')
    assert len(olavo.especialidades) == 2
    print('CORRETO: Especialidades Medico')
except Exception:
    print('ERRADO...: Especialidades não adicionadas')

try:
    # Especialidade exercida na clinica
    olavo.especialidade_exercida('Urologista')
    assert olavo.exerce == 'Urologista'
    print('CORRETO: Especialidade exercida correta')
except Exception:
    print('ERRADO...: Especialidade exercida')

try:
    # Criação do objeto Quarto
    quarto1 = Quarto(1, 1)
    assert quarto1.numero == 1
    assert quarto1.andar == 1
    print('CORRETO: Criação do objeto Quarto')
except Exception:
    print('ERRADO...: Criação do objeto Quarto')

try:
    # Criação do objeto Paciente
    weslley = Paciente('Weslley R.', '123456789-10', 11932445643,
                       '123456789', 'av. rio branco', '16/08/1999',
                       olavo, quarto1)
    assert weslley.nome == 'Weslley R.'
    assert weslley.medico.nome == 'Olavo R.'
    assert weslley.quarto.andar == 1
    assert weslley.quarto.numero == 1
    print('CORRETO: Criação do objeto Paciente')
except Exception:
    print('ERRADO...: Criação do objeto Paciente')

try:
    # Exibição dos metodos get
    assert weslley.get_endereco() == 'av. rio branco'
    assert weslley.get_rg() == '123456789'
    print('CORRETO: Metodo get Paciente')
except Exception:
    print('ERRADO...: Metodo get Paciente')


try:
    # Criação do objeto Visita
    visita1 = Visitas('13/05/2022', quarto1, 'O paciente se encontra estavel',
                      olavo)
    assert visita1.data == '13/05/2022'
    assert visita1.quarto.numero == 1
    assert visita1.registro == 'O paciente se encontra estavel'
    assert visita1.medico.nome == "Olavo R."
    print('CORRETO: Criação do objeto Visita')
except Exception:
    print('ERRADO...: Criação do objeto Visita')

try:
    # Adicionando visita ao paciente
    weslley.adicionar_visita(visita1)
    assert len(weslley.visitas) == 1
    print('CORRETO: Metodo Adicionar_Visita Paciente')
except Exception:
    print('CORRETO: Metodo Adicionar_Visita Paciente')

try:
    # Criação do objeto Clinica
    sao_luis = Clinica()
    sao_luis.adicionar_medicos(olavo)
    sao_luis.adicionar_pacientes(weslley)
    assert len(sao_luis.medicos) == 1
    assert len(sao_luis.pacientes) == 1
    print('CORRETO: Criação do objeto Clinica')
except Exception:
    print('ERRADO...: Criação do objeto Clinica')
