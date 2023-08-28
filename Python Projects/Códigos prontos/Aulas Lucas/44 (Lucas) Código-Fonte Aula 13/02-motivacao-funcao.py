MAX = 10

a = []

def imprime_lista():
    # Imprimindo a lista a
    for i in range(MAX):
        print(a[i], end="")
        if i < MAX - 1:
            print(" - ", end="")
    print()



# Preencher a lista com o valor do índice
for i in range(MAX):
    a.append(i)

imprime_lista()

# Somando dois a cada elemento de a
for i in range(MAX):
    a[i] += 2

imprime_lista()

# Zerando os valores pares de A
for i in range(0, MAX, 2):
    a[i] = 0

imprime_lista()