# Tratamento de erros

try:
    a = int(input("Primeiro numero"))
    b = int(input("Segundo numero"))
    if a < 0 or b < 0:
        raise TypeError  # Gera uma exceção
    c = a / b
    print('Resultado: ', c)
except TypeError:
    print('Erro: o numero informado nao é positivo.')
except ValueError:
    print('Erro. O valor informado não é inteiro.')
except ZeroDivisionError:
    print('Erro: Não é possivel dividir por zero.')
except Exception:
    print('Erro inesperado.')
