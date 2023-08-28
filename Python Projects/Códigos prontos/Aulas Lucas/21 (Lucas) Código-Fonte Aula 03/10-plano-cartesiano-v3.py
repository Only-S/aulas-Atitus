'''
Programa que determina a localização de um ponto no plano cartesiano
'''
x, y = input("Informe as coordenadas do ponto: ").split(" ")
x, y = int(x), int(y)

# Verifica se o ponto está na origem
if x == 0:
    if y == 0: # Como x é 0, então o ponto está na origem ou no eixo y
        print("Ponto na origem")
    else:   # O ponto só pode estar no eixo y
        print("Ponto sobre o Eixo y")
else:   # Se entrar aqui, temos certeza que x != 0
    if y == 0: # O ponto está no eixo x
        print("Ponto sobre o Eixo x")
    else: # só sobraram os quadrantes!
        if x > 0: # quadrantes 1 ou 4, dependendo de y
            if y > 0:  # quadrante 1
                print("Quadrante 1")
            else: # quadrante 4, sem precisar mais testes
                print("Quadrante 4")
        else: #  x é < 0: sobraram quadrantes 2 e 3, dependendo de y
            if y > 0:
                print("Quadrante 2")
            else: # // sobrou x < 0 e y < 0: não precisa testar
                print("Quadrante 3")
