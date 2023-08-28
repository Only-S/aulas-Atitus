'''
Calcula a quantidade de cada cédula (ou moeda) tal que a soma dos valores totalize um valor inteiro dado.
ENTRADA: valor inteiro
SAÍDA  : quantidade de cédulas/moedas de 100, 50, 20, 10, 5, 2 e 1 reais
'''

valor = int(input("Informe um valor inteiro: "))

v = valor # Faz uma cópia para preservar o valor lido

n100 = v // 100 # Divisão inteira por 100
v = v % 100     # Resto da divisão inteira

n50 = v // 50
v = v % 50

n20 = v // 20
v = v % 20

n10 = v // 10
v = v % 10

n5 = v // 5
v = v % 5

n2 = v // 2
n1 = v % 2

# Quebra 2 linhas e escreve a saída do problema
print(f"\n\nValor lido: R${valor},00")
print(f"notas de 100: {n100}")
print(f"notas de 50: {n50}")
print(f"notas de 20: {n20}")
print(f"notas de 10: {n10}")
print(f"notas de 5: {n5}")
print(f"notas de 2: {n2}")
print(f"notas de 1: {n1}")
