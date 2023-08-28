'''
Programa que calcula o fatorial de um número. Realiza a validação para garantir que o número informado é positivo. Repete o cálculo até que o usuário decida parar o programa
'''
resposta = "sim"

while resposta == "sim":
    n = int(input("Informe um número positivo: "))

    while n < 0:
        n = int(input("VALOR INVÁLIDO! Informe um número positivo: "))

    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1

    print(f"FAT = {fat}")

    resposta = input("Calcular o fatorial de outro número [sim] ou [nao]? ")