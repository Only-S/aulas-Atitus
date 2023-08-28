matriz = [[1, 3], [8, -1], [0, -3]]

matriz.append([1, -1])

print(matriz[0].pop())

# Imprimindo a lista no formato de matriz
for linha in matriz:
    for coluna in linha:
        print(f"{coluna:3}", end="")
    print()