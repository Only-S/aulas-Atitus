baralho = {}
i = 1

continuar = True
while continuar:
    print(f"Informe os dados da carta {i}")
    nome = input("Nome: ")
    if nome in baralho.keys():
        print("Já existe uma carta com esse nome!")
        continue

    carta = {}
    carta["tipo"] = input("Tipo: ") # grama, água ou fogo
    carta["hp"] = int(input("HP: "))
    carta["fraqueza"] = input("Fraqueza: ") # grama, água ou fogo

    if carta in baralho.values():
        print("Já existe uma carta com essas características!")
        continue

    baralho[nome] = carta
    continuar = input("Inserir outra carta (s/n)? ").lower() in ['s', 'sim']
    i += 1

print("Seu baralho ficou assim:")
for hashmon, poderes in baralho.items():
    print(f"{hashmon} -> {poderes}")