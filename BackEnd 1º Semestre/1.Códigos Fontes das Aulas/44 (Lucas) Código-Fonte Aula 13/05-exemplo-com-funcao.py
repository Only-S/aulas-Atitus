TAMANHO = 20

def imprime_cabecalho():
    print("+", end="")
    for i in range(TAMANHO):
        print("-", end="")
    print("+")


imprime_cabecalho()

print(" Números entre 1 e 5")

imprime_cabecalho()

for i in range(1, 6):
    print(" ", i)

imprime_cabecalho()