'''
Outras funções da biblioteca random
'''
import random

print("Função uniform")

rnd = random.uniform(1, 10)
print(rnd)

rnd = random.uniform(-10, 10)
print(rnd)

cores = ['amarelo', 'azul', 'vermelho', 'preto', 'verde', 'branco']

print("Função choice")

cor = random.choice(cores)
print(f"Cor escolhida: {cor}")

cor = random.choice(cores)
print(f"Cor escolhida: {cor}")

print("Função sample")

print(f"Amostra 1 = {random.sample(cores, 3)}")
print(f"Amostra 2 = {random.sample(cores, 2)}")
print(f"Amostra 3 = {random.sample(cores, 5)}")

print("Função shuffle")

random.shuffle(cores)
print(f"Embaralhando 1: {cores}")

random.shuffle(cores)
print(f"Embaralhando 2: {cores}")

random.shuffle(cores)
print(f"Embaralhando 3: {cores}")
