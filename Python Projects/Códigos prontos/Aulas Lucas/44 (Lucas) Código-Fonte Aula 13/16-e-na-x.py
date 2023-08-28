import matematica_e
import math

x = float(input("Informe o valor de x: "))
e_x = matematica_e.EnaX(x)

print(f"e^{x} = {e_x}")
print(f"Valor real: {math.exp(x)}")
print(f"ERRO ABSOLUTO: {abs(e_x - math.exp(x))}")