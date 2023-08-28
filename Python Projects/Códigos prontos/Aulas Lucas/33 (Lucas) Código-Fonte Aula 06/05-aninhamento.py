'''
Programa que exemplifica o uso de laços de repetição aninhados
'''
i = 0
while i != 10:
    print("Laço externo")
    j = 0
    for j in range(10):
        print(" - Laço interno")

    i += 1