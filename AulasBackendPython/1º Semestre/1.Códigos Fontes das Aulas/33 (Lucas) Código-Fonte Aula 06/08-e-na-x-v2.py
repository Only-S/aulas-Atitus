'''
Programa para calcular exp(x), aproximando o resultado por uma série de potência
ENTRADA: x e número de termos da série
SAÍDA  : exp(x)
'''
import math

x = float(input("Informe o valor de x: "))
n = int(input("Informe o número de termos da série: "))

exp_x = 0
fat = 1
for i in range(1, n):
    fat = fat * i    
    termo = (x ** i) / fat
    exp_x += termo
    print(f"Valor calculado até a iteração {i}: {exp_x}")

print(f"Valor calculado de exp({x:.2f}) = {exp_x}")
print(f"Valor de exp({x:.2f})           = {math.exp(x)}")


