'''
Programa que calcula o fatorial de um número
'''
n = int(input("Informe um número positivo: "))

fat = 1
while n > 1:
    fat = fat * n
    n = n - 1

print(f"FAT = {fat}")