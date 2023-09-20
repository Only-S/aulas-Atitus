'''
Programa que calcula a altura de uma escada encostada em uma parede, dados o ângulo da escada e a altura da parede
'''
import math

angulo = float(input("Informe o ângulo da escada com o chão (em graus): "))
parede = float(input("Informe a altura da parede (em metros): "))

# Converte o ângulo para radianos
radianos = angulo * math.pi / 180

escada = parede / math.sin(radianos)

print(f"A altura da escada é de {escada:.2f} metros")