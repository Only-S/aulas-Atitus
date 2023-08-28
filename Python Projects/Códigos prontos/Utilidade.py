#Contador - Algoritmo que conta quantos alunos foram aprovados.
aprovados = 0
for i in range(10):
    media = float(input(f"Nota do aluno {i + 1}: "))
    if media > 7:
        aprovados += 1

print(f"Total de aprovados: {aprovados}")

#Acumulador - Algoritmo que soma as despesas de uma pessoa até que digite 0
despesas = 0
valor = 1
while valor != 0:
    valor = float(input("Informe a despesa (0 p/ sair): "))
    despesas += valor
print(f"Total Despesas: R${despesas:.2f}")

#Flag - Algoritmo que determina se um número é primo
nao_eh_primo = False
valor = int(input("Digite um número: "))
for div in range(2, valor):
    if valor % div == 0:
        nao_eh_primo = True

if nao_eh_primo:
    print("O número não é primo")
else:
    print("O número é primo")

#Programa que lê 5 idades e mostra o somatório, quantas idades menores de 18 e quantas se há idades entre 60 e 65
soma = 0 # Acumulador
cont = 0 # Contador
digitou_60 = False # Flag
for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    soma += idade # Usa o acumulador para somar idades
    if idade < 18:
        cont += 1 # Conta pessoas menores de idade
    if idade >= 60 and idade <= 65:
        digitou_60 = True # Modifica o valor da flag caso a idade esteja no intervalo

print(f"Somatório das idades: {soma} anos")
print(f"Foram informadas {cont} idades inferiores a 18 anos")
if digitou_60:
    print("Foram informadas idades entre 60 e 65 anos.")
else:
    print("NÃO foram informadas idades entre 60 e 65 anos.")

#Aninhamento de Laço - Algoritmo que le notas de 10 alunos
for i in range(1, 11):
    nota = -1
    while nota < 0 or nota > 10:
        nota = float(input(f"Nota do aluno {i}: "))

#Variável string como lista
palavra = input('Digite uma palavra: ')
p1 = [l for l in palavra if l != 'a' and l != 'e' and l != 'i' and l != 'o' and l != 'u']
print(p1)

#Lista de números entre 1 e 100 divisiveis por 3
num = []

for n in range(1, 101):
    if n % 3 == 0:
        num.append(n)

print(num)

#Algoritmo que calcula a média da turma baseado na 1ª nota de cada uma das 4 notas dos alunos e vonta quantos ficaram acima da média.
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