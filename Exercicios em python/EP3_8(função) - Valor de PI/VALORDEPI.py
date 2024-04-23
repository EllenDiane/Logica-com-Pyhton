def calcular_pi(n):
    pi = 0
    for i in range(n):
        conta = (-1) ** i * (2 * i + 1)
        pi += 4 / conta

    return pi