'''
Programa que conta quantos alunos foram aprovados em uma turma
OBS: Média para passar == 7
'''

aprovados = 0
for i in range(10):
    media = float(input(f"Nota do aluno {i + 1}: "))
    if media > 7:
        aprovados += 1

print(f"Total de aprovados: {aprovados}")

