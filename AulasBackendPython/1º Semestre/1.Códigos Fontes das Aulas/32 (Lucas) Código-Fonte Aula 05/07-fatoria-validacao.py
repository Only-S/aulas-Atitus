'''
Programa que calcula o fatorial de um número. Realiza a validação para garantir que o número informado é positivo.
'''
n = int(input("Informe um número positivo: "))

while n < 0:
    n = int(input("VALOR INVÁLIDO! Informe um número positivo: "))

fat = 1
while n > 1:
    fat = fat * n
    n = n - 1

print(f"FAT = {fat}")