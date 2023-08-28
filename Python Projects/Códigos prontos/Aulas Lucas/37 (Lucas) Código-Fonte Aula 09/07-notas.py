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

print(f"{cont_alunos} alunos tiveram nota acima da média")
