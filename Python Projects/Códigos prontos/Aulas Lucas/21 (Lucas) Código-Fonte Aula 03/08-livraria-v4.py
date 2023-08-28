'''
Programa que processa uma venda e avisa caso tenha sido vendidas mais de 10 unidades
'''
PRECO_A = 10
PRECO_B = 20
PRECO_C = 30

codigo = input("Informe o tipo do livro (A, B ou C): ")
quantidade = int(input("Informe a quantidade vendida: "))

codigo = codigo.upper()

if codigo == "A":
    total = quantidade * PRECO_A
elif codigo == "B":
        total = quantidade * PRECO_B
elif codigo == "C":
    total = quantidade * PRECO_C
else:
    total = 0
    print("Código Inexistente!")

if total != 0:
    print(f"Total a ser pago: R${total:6.2f}")

    if quantidade > 10:
        print(f"Foram vendidos mais de 10 livros do tipo {codigo}")