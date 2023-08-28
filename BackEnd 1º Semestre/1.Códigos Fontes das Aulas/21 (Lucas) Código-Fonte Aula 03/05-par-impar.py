'''
Programa que analisa se um número natural lido é par ou ímpar
'''

valor = int(input("Digite o valor a ser testado: "))

if valor % 2 == 0:
    print(f"{valor} é par!")
else:
    print(f"{valor} é ímpar!")