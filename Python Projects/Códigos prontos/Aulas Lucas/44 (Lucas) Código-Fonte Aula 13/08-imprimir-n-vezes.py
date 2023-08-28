
def imprimir(caracter, vezes):
    print(caracter * vezes)


char = 'a'
repeticoes = 1
incremento = 1
while repeticoes > 0:
    imprimir(char, repeticoes)
    repeticoes += incremento
    char = chr(ord(char) + 1)

    if char == 'l':
        print('-> ', end="")
        incremento = -1

