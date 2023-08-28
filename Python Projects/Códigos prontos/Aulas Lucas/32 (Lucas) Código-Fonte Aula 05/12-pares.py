'''
Programa que mostra os números pares existentes entre dois valores informados
'''
inicio, fim = input("Informe o início e o fim do intervalo: ").split(" ")
inicio, fim = int(inicio), int(fim)

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        print(f"{i} ", end="")