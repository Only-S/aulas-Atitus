'''
Programa que processa uma venda e avisa caso tenha sido vendidas mais de 10 unidades
'''
PRECO_A = 10
PRECO_B = 20
PRECO_C = 30

codigo = input("Informe o tipo do livro (A, B ou C): ")
quantidade = int(input("Informe a quantidade vendida: "))

if codigo == "a" or codigo == "A":
    total = quantidade * PRECO_A
else:
    if codigo == "b" or codigo == "B":
        total = quantidade * PRECO_B
    else:
        if codigo == "c" or codigo == "C":
            total = quantidade * PRECO_C
        else:
            print("Código Inexistente!")

print(f"Total a ser pago: R${total:6.2f}")

if quantidade > 10:
    print(f"Foram vendidos mais de 10 livros do tipo {codigo}")