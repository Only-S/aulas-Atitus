'''
Programa que obtem as notas de 30 alunos e informa a média da turma. 
'''
ALUNOS = 30

soma = 0
for aluno in range(ALUNOS):
    nota = float(input("Informe a nota: "))
    soma += nota

media = soma / ALUNOS
print(f"MÉDIA DA TURMA: {media:.2f}")