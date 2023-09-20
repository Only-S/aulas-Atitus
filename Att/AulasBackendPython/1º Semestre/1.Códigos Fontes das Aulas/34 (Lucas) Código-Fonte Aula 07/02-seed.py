'''
Uso de seed para gerar a mesma sequência de valores aleatórios
'''
import random

print("Os números sorteados são:")

# Configurando a semente aleatória
random.seed(100)

rnd = random.randint(1, 10)
print(rnd)

rnd = random.randint(0, 100)
print(rnd)

rnd = random.randint(-100, 100)
print(rnd)
