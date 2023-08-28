import random

NL = 5
NC = 3

# Preenchendo a matriz com valores entre -10 e 10
matriz = []
for i in range(NL):
    linha = []
    for j in range(NC):
        valor = random.randint(-10, 10)
        linha.append(valor)
    matriz.append(linha)

# Imprimindo a matriz gerada
for linha in matriz:
    for valor in linha:
        print(f"{valor:4}", end="")
    print()

# Média dos elementos de cada linha
for i, linha in enumerate(matriz):
    soma = 0
    for valor in linha:
        soma += valor
    media = soma / NC
    print(f"A média da linha {i} é {media:.2f}")

print()

# Buscar o maior elemento de cada coluna
for coluna in range(NC):
    maior = matriz[0][coluna]
    for linha in range(1, NL):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
    print(f"Maior elemento da coluna {coluna} é {maior}")

# Produto dos elementos diferentes de zero
produto = 1
for linha in matriz:
    for valor in linha:
        if valor != 0:
            produto *= valor
print(f"O Produto dos elementos não nulos é {produto}")

# Quantidade de elementos negativos
contador = 0
for linha in matriz:
    for valor in linha:
        if valor < 0:
            contador += 1
print(f"Existem {contador} elementos negativos na matriz")

# Busca na matriz
valor_buscado = int(input("Informe o valor: "))
achou = False
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        if valor == valor_buscado:
            print(f"{valor} encontrado na posição [{i}][{j}]")
            achou = True
if not achou:
    print("Valor não encontrado!")