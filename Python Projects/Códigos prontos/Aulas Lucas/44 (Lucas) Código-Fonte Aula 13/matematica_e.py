def fatorial(numero):
    fat = 0
    if numero > 0:
        fat = 1
        for i in range(numero, 1, -1):
            fat *= i
    return fat

def potencia(x, n):
    pot = 1
    for i in range(n):
        pot *= x
    return pot

def EnaX(x):
    e = 0
    termo = 1
    n = 0    
    while termo > 0.0001:
        e += termo
        n += 1
        num = potencia(x, n)
        den = fatorial(n)
        termo = num / den
        
    return e
