def imprime_char(inicio, fim):
    letras = []
    for val in range(inicio, fim + 1):
        char = chr(val)
        letras.append(char)
    print(", ".join(letras))

ini = int(input("Inicio do intervalo: "))
fim = int(input("Final do intervalo: "))

if ini < fim:
    imprime_char(ini, fim)
else:
    imprime_char(fim, ini)