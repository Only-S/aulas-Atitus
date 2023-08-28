'''
Programa que lê um código e realiza uma operação de acordo com o valor digitado
Versão 2: Usando o padrão ou "|"
'''
codigo = int(input("Informe o código: "))

resultado = 20
match codigo:
    case 1:
        resultado += 5
    case 3 | 5:
        resultado -= 2
    case 6:
        resultado = 2 * (resultado + 1)
    case 8 | 9 | 10:
        resultado = 0
    case 11:
        resultado = 123
    
print(f"RESULTADO = {resultado}")