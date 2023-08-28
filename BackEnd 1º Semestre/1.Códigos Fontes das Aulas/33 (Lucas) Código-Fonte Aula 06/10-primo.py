'''
Programa que lê um valor (validando a entrada para que ela seja um número inteiro maior ou igual a dois) e informa se esse valor é um número primo
'''
valor = 0
while valor < 2:
    valor = int(input("Informe um valor: "))
    
for div in range(2, valor):
    if valor % div == 0:
        print(f"O número {valor} não é primo")
        break
else:
    print(f"O número {valor} é primo")