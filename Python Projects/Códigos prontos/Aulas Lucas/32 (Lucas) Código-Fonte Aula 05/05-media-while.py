'''
Programa que mostra se um aluno foi aprovado ou não com base na média, para uma turma de 5 alunos, com o comando while
'''
i = 0
while i < 5:
    media = float(input(f"Média do aluno {i + 1}: "))
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    
    i += 1
