'''
Programa que lê a idade de 5 pessoas e mostra:
    - Somatório das idades
    - Quantas idades são menores do que 18 anos
    - Se foi informada uma idade entre 60 e 65 anos
'''
soma = 0 # Acumulador
cont = 0 # Contador
digitou_60 = False # Flag

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    soma += idade # Usa o acumulador para somar idades

    if idade < 18:
        cont += 1   # Conta pessoas menores de idade

    if idade >= 60 and idade <= 65:
        digitou_60 = True   # Modifica o valor da flag caso a idade esteja no intervalo

print(f"Somatório das idades: {soma} anos")
print(f"Foram informadas {cont} idades inferiores a 18 anos")
if digitou_60:
    print("Foram informadas idades entre 60 e 65 anos.")
else:
    print("NÃO foram informadas idades entre 60 e 65 anos.")