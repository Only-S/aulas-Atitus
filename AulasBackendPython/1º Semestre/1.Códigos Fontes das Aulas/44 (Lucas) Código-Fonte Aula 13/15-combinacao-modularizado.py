import matematica

n = int(input("Informe o valor de n (número de elementos): "))
p = int(input("Informe o valor de p (qtde elementos por grupo): "))

comb = matematica.combinacoes(n, p)
print(f"Combinações de {n} valores {p} a {p} = {comb}")