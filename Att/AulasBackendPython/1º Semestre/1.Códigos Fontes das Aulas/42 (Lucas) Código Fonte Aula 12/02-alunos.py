pcomp = set()
ia = set()
des_prof = set()

nome = " "
while nome != "":
    nome = input("Informe um aluno de Pensamento Computacional (ou nada para terminar): ")
    if nome != "":
        pcomp.add(nome)

nome = " "
while nome != "":
    nome = input("Informe um aluno de Inteligência Artificial (ou nada para terminar): ")
    if nome != "":
        ia.add(nome)

nome = " "
while nome != "":
    nome = input("Informe um aluno de Desafios da Profissão (ou nada para terminar): ")
    if nome != "":
        des_prof.add(nome)

print("Alunos que cursam Inteligência Artificial E Desafios da Profissão:")
for aluno in ia.intersection(des_prof):
    print(f"  - {aluno}")

print("Alunos que cursam Pensamento Computacional OU Inteligência Artificial:")
for aluno in pcomp.union(ia):
    print(f"  - {aluno}")

print("Alunos que cursam Pensamento Computacional mas NÃO Desafios da Profissão:")
for aluno in pcomp.difference(des_prof):
    print(f"  - {aluno}")
    