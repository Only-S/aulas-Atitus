def menu_de_opcoes():
    print("-" * 10)
    print("MENU".center(10))
    print("-" * 10)
    print()
    print("  1 - Soma de dois valores reais")
    print("  2 - Divisores do número")
    print("  3 - Sequência de números pares ")
    print("  4 - Verifica se o número é perfeito")

    print("\nInforme a opção desejada:")
    opcao = int(input("\t? "))
    if opcao >= 1 and opcao <= 4: 
        return opcao
    else:
        return -1

op = menu_de_opcoes()
if op != -1:
    print(f"Opção escolhida: {op}")
else:
    print("Opção Inválida!")

