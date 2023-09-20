import random

VALORES = 20000

vetor = []

# Preenche o vetor
for i in range(VALORES):
    numero = random.randint(1000, 100000)
    vetor.append(numero)

# Encontra o maior
maior = vetor[0]
posicao_maior = 0 
pos = 1
while pos < VALORES:
    if vetor[pos] > maior:
        maior = vetor[pos]
        posicao_maior = pos
    pos += 1

print(f"O maior valor do vetor está na posição {posicao_maior} e é o valor {maior}")


# Encontra o menor
menor = vetor[0]
posicao_menor = 0 
pos = 1
while pos < VALORES:
    if vetor[pos] < menor:
        menor = vetor[pos]
        posicao_menor = pos
    pos += 1

print(f"O menor valor do vetor está na posição {posicao_menor} e é o valor {menor}")

# Valor médio
soma = 0
for val in vetor:
    soma += val
media = soma / VALORES
print(f"Valor médio = {media}")

prox_media = vetor[0]
diff_media = abs(media - prox_media)
posicao_media = 0
pos = 1
while pos < VALORES:
    if abs(media - vetor[pos]) < diff_media:
        diff_media = abs(media - vetor[pos])
        posicao_media = pos
        prox_media = vetor[pos]
    pos += 1

print(f"O valor mais proximo da media está na posicao {posicao_media} e é o valor {prox_media}")