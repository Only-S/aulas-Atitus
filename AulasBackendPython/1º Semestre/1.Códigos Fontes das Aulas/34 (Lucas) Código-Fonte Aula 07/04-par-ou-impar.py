'''
Jogo de par ou ímpar
'''

import random

# Lê a opção
opcao = ''
while opcao != 'p' and opcao != 'i':
    opcao = input("[P]ar ou [I]mpar? ")
    opcao = opcao.lower()
    if opcao != 'p' and opcao != 'i':
        print("Opção inválida! ", end="")

# Lê a jogada e escolhe o número aleatório
humano = int(input("Escolha um número: "))
computador = random.randint(0, 10)
print(f"O computador escolheu: {computador}")
total = humano + computador
# Verifica se a soma é par ou ímpar
if total % 2 == 0:
    print("A soma é par! ", end="")
    resultado = 'p'
else:
    print("A soma é ímpar! ", end="")
    resultado = 'i'

if resultado == opcao:
    print("Você ganhou :(")
else:
    print("Eu ganhei! :)")
