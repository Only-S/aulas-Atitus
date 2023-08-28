'''
Calcula a média de uma turma e mostra quais notas ficaram acima da média. 
Entradas: notas de 30 alunos.  
Saida: media da turma e notas acima da média
'''
ALUNOS = 30

# Inicializa uma lista vazia de notas
notas = []
soma = 0

# Obtém a nota de cada aluno 
for aluno in range(ALUNOS):
    nota = float(input(f"Informe a nota do aluno {aluno + 1}: "))
    notas.append(nota)
    soma += nota

# Calcula a média
media = soma / ALUNOS

# Escreve a média
print(f"Media da turma: {media:.2f}")

# Escreve as notas acima da média
for nota in notas:
    if nota > media: 
        print(nota)
