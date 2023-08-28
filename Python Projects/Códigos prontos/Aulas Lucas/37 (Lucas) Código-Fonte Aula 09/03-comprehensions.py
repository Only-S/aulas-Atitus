lista = []
for i in range(1, 6):
    lista.append(i)

print(lista)

lista = [i for i in range(1, 6)]
print(lista)

# Mapeamento

lista = [i ** 2 for i in range(1, 6)]
print(lista)

# Filtragem
lista = [i for i in range(1, 6) if i % 2 == 0]
print(lista)


cores = ["azul", "vermelho", "amarelo", "verde"]
novas_cores = [cor.upper() for cor in cores]

print(f"novas_cores = {novas_cores}")
print(f"cores = {cores}")