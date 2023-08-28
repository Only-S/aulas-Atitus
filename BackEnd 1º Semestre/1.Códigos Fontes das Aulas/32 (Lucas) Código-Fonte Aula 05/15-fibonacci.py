'''
Programa que mostra o termo correspondente da sequência de Fibonacci.
'''
pos = int(input("Entre com o termo desejado: "))

if pos < 0:
    print("A posição não pode ser negativa!")
else:
    if pos == 0:
        fib = 0
    elif pos == 1:
        fib = 1
    else:
        t_2 = 0
        t_1 = 1
        for i in range(2, pos + 1):
            fib = t_2 + t_1
            t_2 = t_1
            t_1 = fib
    print(f"O termo {pos} da série de Fibonacci é {fib}")