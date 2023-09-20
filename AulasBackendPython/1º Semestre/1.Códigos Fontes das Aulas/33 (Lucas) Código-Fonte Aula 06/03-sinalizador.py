'''
Programa que verifica se um número informado é primo ou não
'''
nao_eh_primo = False

valor = int(input("Digite um número: "))

for div in range(2, valor):
    if valor % div == 0:
        nao_eh_primo = True

if nao_eh_primo:
    print("O número não é primo")
else:
    print("O número é primo")