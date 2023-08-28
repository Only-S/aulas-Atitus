n = 123 #n recebe valor inteiro 123
aux1 = n % 10 #aux1 recebe n módulo 10 =  3
aux2 = n // 10 #aux2 recebe a divisão inteira n por 10 = 12
aux3 = aux2 % 10 #aux3 recebe 12 módulo 10 = 2
aux2 = aux2 // 10 #aux2 recebe a divisão inteira de 12 por 10 = 1
n = aux1 * 100 #n recebe 3 x 100 = 300
n = n + aux2 * 10 #n recebe a si mesmo + 12 = 310
n = n + aux3 #n recebe a si mesmo + 2 = 312
print(n)
