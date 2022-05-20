from distutils.log import error


def soma(a, b):
    c = a + b
    return c


def quadrado(a):
    return a*a


def soma_dos_quadrados(a, b):
    a = quadrado(a)
    b = quadrado(b)
    return a + b


def media(a, b, c):
    return (a + b + c) / 3


def calcular_salario(salario):
    if salario > 2000:
        newSalario = (salario * 0.07) + salario
        return newSalario
    else:
        newSalario = (salario * 0.15) + salario
        return newSalario


def soma_divisores(n):
    if n < 0:
        return error("Numero negativo!")
