def fatorial(numero):
    fat = 0
    if numero > 0:
        fat = 1
        for i in range(numero, 1, -1):
            fat *= i
    return fat

def combinacoes(n, p):
    return fatorial(n) / (fatorial(p) * fatorial(n - p))

n = int(input("Informe o valor de n (número de elementos): "))
p = int(input("Informe o valor de p (qtde elementos por grupo): "))

comb = combinacoes(n, p)
print(f"Combinações de {n} valores {p} a {p} = {comb}")