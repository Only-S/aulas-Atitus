def fatorial(numero):
    fat = 0
    if numero > 0:
        fat = 1
        for i in range(numero, 1, -1):
            fat *= i
    return fat

def combinacoes(n, p):
    return fatorial(n) / (fatorial(p) * fatorial(n - p))