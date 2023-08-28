lista = [1, 2, 3, 4, 5]

outra_lista = lista
print("Antes da atribuição:")
print(f"lista = {lista} - outra_lista = {outra_lista}")

outra_lista[0] = "zero"

print("Depois da atribuição:")
print(f"lista = {lista} - outra_lista = {outra_lista}")