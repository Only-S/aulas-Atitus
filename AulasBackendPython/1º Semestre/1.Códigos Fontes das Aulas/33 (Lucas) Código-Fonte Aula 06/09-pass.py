'''
Programa que ilustra o uso do comando pass
'''
valor = 0
while valor >= 0:
    valor = int(input("Informe um valor: "))
    if valor < 10:
        pass
    else:
        print("Você digitou um número muito alto!")