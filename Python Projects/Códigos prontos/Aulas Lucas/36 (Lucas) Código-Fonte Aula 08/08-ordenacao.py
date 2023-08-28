lista = [12, 7, 97, -4, 3, 78, 14, 94, -11]

op = input("Ordem crescente (c) ou decrescente (d)? ")

if op == "c":
    lista.sort()
    print(lista)
elif op == "d":
    lista.sort(reverse=True)
    print(lista)
else:
    print("Opção Inválida!")