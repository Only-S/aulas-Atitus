'''
Programa que determina a localização de um ponto no plano cartesiano
'''
x, y = input("Informe as coordenada do ponto: ").split(" ")
x, y = int(x), int(y)

if x == 0 and y == 0:
    print("Ponto na origem")
elif x > 0 and y > 0:
    print("Quadrante 1")
elif x < 0 and y > 0:
    print("Quadrante 2")
elif x < 0 and y < 0:
    print("Quadrante 3")
elif x > 0 and y < 0:
    print("Quadrante 4")
elif x != 0 and y == 0:
    print("Ponto sobre o Eixo x")
elif x == 0 and y != 0:
    print("Ponto sobre o Eixo y")