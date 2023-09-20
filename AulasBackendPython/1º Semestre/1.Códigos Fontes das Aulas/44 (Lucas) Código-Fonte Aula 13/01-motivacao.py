MAX = 10

a = []

# Preencher a lista com o valor do índice
for i in range(MAX):
    a.append(i)

# Imprimindo a lista a
for i in range(MAX):
    print(a[i], end="")
    if i < MAX - 1:
        print(" - ", end="")
print()

# Somando dois a cada elemento de a
for i in range(MAX):
    a[i] += 2

# Imprimindo a lista a
for i in range(MAX):
    print(a[i], end="")
    if i < MAX - 1:
        print(" - ", end="")
print()

# Zerando os valores pares de A
for i in range(0, MAX, 2):
    a[i] = 0

# Imprimindo a lista a
for i in range(MAX):
    print(a[i], end="")
    if i < MAX - 1:
        print(" - ", end="")
print()