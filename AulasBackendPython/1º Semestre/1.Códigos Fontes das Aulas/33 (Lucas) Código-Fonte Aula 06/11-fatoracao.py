'''
Programa que mostra os fatores primos de um número informado
'''
valor = 0
while valor < 2:
    try:
        valor = int(input("Informe um valor: "))
    except ValueError:
        pass

div = 2
while valor > 1:
    if valor % div == 0:
        print(f"{valor:4} | {div}")
        valor = valor // div
        continue
    div += 1

print(f"{valor:4}")