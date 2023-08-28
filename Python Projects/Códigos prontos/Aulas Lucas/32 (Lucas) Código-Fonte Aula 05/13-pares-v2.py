'''
Programa que mostra os números pares existentes entre dois valores informados. Versão otimizada que usa um range com passo 2.
'''
inicio, fim = input("Informe o início e o fim do intervalo: ").split(" ")
inicio, fim = int(inicio), int(fim)

if inicio % 2 != 0: # Garante que o primeiro valor do intervalo é par
    inicio += 1

for i in range(inicio, fim + 1, 2):
    print(f"{i} ", end="")