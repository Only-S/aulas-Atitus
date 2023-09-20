'''
Programa que determina a localização de um ponto no plano cartesiano
'''
x, y = input("Informe as coordenada do ponto: ").split(" ")
x, y = int(x), int(y)

if x == 0 and y == 0:
    print("Ponto na origem")
if x > 0 and y > 0:
    print("Quadrante 1")
if x < 0 and y > 0:
    print("Quadrante 2")
if x < 0 and y < 0:
    print("Quadrante 3")
if x > 0 and y < 0:
    print("Quadrante 4")
if x != 0 and y == 0:
    print("Ponto sobre o Eixo x")
if x == 0 and y != 0:
    print("Ponto sobre o Eixo y")