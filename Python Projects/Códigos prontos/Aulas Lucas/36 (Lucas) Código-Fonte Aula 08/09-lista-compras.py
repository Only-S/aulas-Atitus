
compras = []

# Mostra o menu
print("===== LISTA DE COMPRAS ====")
print("[1] Inserir item")
print("[2] Remover item")
print("[3] Remover itens duplicados")
print("[4] Ordenar a lista em ordem alfabética")
print("[5] Imprimir a lista de compras")
print("[6] Esvaziar a lista")
print("[99] SAIR")

opcao = int(input("Informe sua opção: "))

while opcao != 99:
    match opcao:
        case 1: # Inserir item
            item = input("Informe o nome do produto: ")
            compras.append(item)

        case 2: # Remover item
            op = ""
            while op != "c" and op != "p":
                op = input("Remover por [c]onteúdo ou por [p]osição? ")
            
            if op == "c":
                item = input("Informe o item a ser removido: ")
                if item in compras:
                    compras.remove(item)
                    print(f"O item {item} foi removido da lista!")
                else:
                    print(f"O item {item} não está na lista!")
            else:
                pos = int(input(f"Informe a posicao que você quer remover [inteiro entre 0 e {len(compras) - 1}]: "))
                if pos < 0 or pos >= len(compras):
                    print("Posição inválida!")
                else:
                    item = compras.pop(pos)
                    print(f"O item {item} foi removido da lista!")
        
        case 3: # Remover itens duplicados
            for item in compras:
                if compras.count(item) > 1:
                    compras.remove(item)
                    print(f"O item {item} foi removido da lista!")
        
        case 4: # Ordenar a lista em ordem alfabética
            ordem = ""
            while ordem != "c" and ordem != "d":
                ordem = input("Ordenar [c]rescente ou [d]ecrescente? ")
            
            if ordem == "c":
                compras.sort()
            else:
                compras.sort(reverse=True)
            print("Lista ordenada! Use a opção 5 para imprimir toda a lista e veja o resultado.")
        
        case 5: # Imprimir a lista de compras
            print("-" * 10, "LISTA DE COMPRAS", "-" * 10)
            for item in compras:
                print(f"- {item}")
            print("-" * 38)

        case 6: # Esvaziar a lista
            compras.clear()
            print("A lista foi esvaziada")

    # Mostra o menu
    print("===== LISTA DE COMPRAS ====")
    print("[1] Inserir item")
    print("[2] Remover item")
    print("[3] Remover itens duplicados")
    print("[4] Ordenar a lista em ordem alfabética")
    print("[5] Imprimir a lista de compras")
    print("[6] Esvaziar a lista")
    print("[99] SAIR")

    opcao = int(input("Informe sua opção: "))
