
zodiaco = ('Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Cobra', 'Cavalo', 'Cabra', 'Macaco', 'Galo', 'Cachorro', 'Porco')

print("Este programa mostra o seu signo no Horóscopo Chinês")

fim = False
while not fim:
    # Lê o ano de nascimento
    ano_nasc = int(input('Informe o ano de nascimento (yyyy): '))

    while ano_nasc < 1900:
        ano_nasc = int(input('ENTRADA INCORRETA! Informe o ano de nascimento (yyyy): '))
    
    signo = (ano_nasc - 1900) % 12

    print(f"\nSeu signo é {zodiaco[signo].upper()}\n")

    fim = input("Informar outro ano [S]im ou [N]ão? ").lower() != "s"
    
