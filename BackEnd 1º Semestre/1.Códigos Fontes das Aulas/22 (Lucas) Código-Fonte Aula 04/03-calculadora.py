'''
Programa que simula uma calculadora, permitindo que oi usuário execute as 4 operações básicas
'''
operando1, operador, operando2 = input("Informe a operação (no formato op + op): ").split(" ")

operando1, operando2 = float(operando1), float(operando2)

erro = False
match operador:
    case "+":
        resultado = operando1 + operando2
    case "-":
        resultado = operando1 - operando2
    case "*":
        resultado = operando1 * operando2
    case "/":
        resultado = operando1 / operando2
    case _:
        print("Operação desconhecida!")
        erro = True

if not erro:
    print(f"{operando1} {operador} {operando2} = {resultado}")