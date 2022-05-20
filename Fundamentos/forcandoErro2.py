def soma_divisores(n):
    a = None
    if n < 0:
        return "erro"
    for i in range(n):
        if n % i == 0:
            a = n + i

    return a


print(soma_divisores(2))
