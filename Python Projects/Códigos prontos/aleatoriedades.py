'''palavra = input('Digite uma palavra: ')
p1 = [l for l in palavra if l != 'a' and l != 'e' and l != 'i' and l != 'o' and l != 'u']
print(p1)

num = []

for n in range(1, 101):
    if n % 3 == 0:
        num.append(n)

print(num)

import random

NRO_ALUNOS = 10
NRO_NOTAS = 4

notas = []

for aluno in range(NRO_ALUNOS):
    notas_aluno = []
    for nota in range(NRO_NOTAS):
        #nt = float(input(f"Informe a nota {nota + 1} do aluno {aluno + 1}: "))
        nt = round(random.uniform(1, 10), 1)
        notas_aluno.append(nt)
    notas.append(notas_aluno)

# Cálculo da média da primeira nota
soma = 0
for aluno in range(NRO_ALUNOS):
    soma += notas[aluno][0]
media = soma / NRO_ALUNOS
print(f"Média da turma na primeira nota: {media:.2f}")

# Contando os alunos que estão acima da média
cont_alunos = 0
for aluno in range(NRO_ALUNOS):
    if notas[aluno][0] > media:
        cont_alunos += 1

print(f"{cont_alunos} alunos tiveram nota acima da média")'''

baralho = {}
i = 1
continuar = True
while continuar:
    print(f"Informe os dados da carta {i}")
    nome = input("Nome: ")
    if nome in baralho.keys():
        print("Já existe uma carta com esse nome!")
        continue
    carta = {}
    carta["tipo"] = input("Tipo: ") # grama, água ou fogo
    carta["hp"] = int(input("HP: "))
    carta["fraqueza"] = input("Fraqueza: ") # grama, água ou fogo
    if carta in baralho.values():
        print("Já existe uma carta com essas características!")
        continue
    baralho[nome] = carta
    continuar = input("Inserir outra carta (s/n)? ").lower() in ['s', 'sim']
    i += 1
print("Seu baralho ficou assim:")
for hashmon, poderes in baralho.items():
    print(f"{hashmon} -> {poderes}")