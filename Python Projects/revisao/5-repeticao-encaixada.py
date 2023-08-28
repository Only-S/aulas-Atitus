d = -4
l = 0
j = 3
for i in range(2, 5): #de 4 a 4
    while j >= 0: #j = 0
        k = i + j #k = 4
        j -= 1 #j = -1
        d += 1 #d = 2
        if d > 0: #D = 2
            j -= d #-3
        print(f"J = {j}, K = {k} L = {l}") #J = 2, K = 5, L = 0 | J = 1, K = 4, L = 0 | J = 0, K = 3, L = 0 | J = -1, K = 2, L = 0 | J = -2, K = 3, L = 2 | J = -3, K = 4, L = 5
    j = 0 #J = 0
    l += i #L = 2
print(f"I = {i}") #valor de i é 4