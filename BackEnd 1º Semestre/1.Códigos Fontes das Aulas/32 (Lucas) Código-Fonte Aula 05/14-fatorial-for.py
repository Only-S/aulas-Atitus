'''
Programa que calcula o fatorial de um número, utilizando o comando for
'''
n = int(input("Informe um número positivo: "))

fat = 1
for i in range(1, n + 1):
    fat = fat * i

print(f"FAT = {fat}")