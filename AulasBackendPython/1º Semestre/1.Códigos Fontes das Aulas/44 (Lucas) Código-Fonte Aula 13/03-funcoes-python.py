import math

circulo = input("Forneça o identificador do círculo: ")
circulo = circulo.upper()

raio = float(input("Forneça o raio do círculo: "))
area = math.pi * math.pow(raio, 2)
print(f"Área do círculo {circulo} de raio {raio:.2f} é {area:.2f}")