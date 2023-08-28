def fibonacci(posicao):
    t_1 = 1
    t_2 = 0
    for i in range(posicao + 1):
        match i:
            case 0:
                fib = 0
            case 1:
                fib = 1
            case _:
                fib = t_2 + t_1
                t_2 = t_1
                t_1 = fib
        print(f"DENTRO FUNÇÃO: fib({i}) = {fib}")
    return fib


pos = int(input("Informe a posição: "))
f = fibonacci(pos)
print(f"PROGRAMA PRINCIPAL: fib({pos}) = {f}")