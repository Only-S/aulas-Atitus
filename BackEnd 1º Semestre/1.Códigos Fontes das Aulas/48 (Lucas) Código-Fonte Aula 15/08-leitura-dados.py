# Garantindo que o número lido esteja no intervalo de 5 até 15
fim = False
while not fim:
    try:
        valor = int(input("Informe um número: "))
        if valor < 5 or valor > 15:
            raise ValueError("O número não está no intervalo correto!")
        fim = True
    except ValueError as excecao:
        print(f"Ocorreu um erro! {excecao}")