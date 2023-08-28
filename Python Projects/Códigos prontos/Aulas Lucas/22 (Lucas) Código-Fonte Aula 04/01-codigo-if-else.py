
'''
Programa que lê um código e realiza uma operação de acordo com o valor digitado
'''
# Lê o código
codigo = int(input("Informe o código: "))

resultado = 20
if codigo == 1:
    resultado += 5
elif codigo == 3 or codigo == 5:
    resultado -= 2
elif codigo == 6:
    resultado = 2 * (resultado + 1)
elif codigo == 8 or codigo == 9 or codigo == 10:
    resultado = 0
elif codigo == 11:
    resultado = 123

print(f"RESULTADO = {resultado}")