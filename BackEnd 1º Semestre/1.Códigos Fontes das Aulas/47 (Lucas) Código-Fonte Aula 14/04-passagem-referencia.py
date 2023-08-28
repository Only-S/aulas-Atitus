def funcao_lista(lista):
    print(f"F1: {lista}")
    lista[0] = 2
    print(f"F2: {lista}")

# Programa Principal
v = [1]
print(f"P1: {v}")    
funcao_lista(v)
print(f"P2: {v}")    