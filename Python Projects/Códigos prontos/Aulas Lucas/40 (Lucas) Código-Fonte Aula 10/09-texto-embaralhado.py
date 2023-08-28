import random

texto = "Os seres humanos são capazes de ler textos onde as letras das palavras estão embaralhadas , contanto que a primeira e a última letra da palavra sejam preservadas"

palavras = texto.split()
saida = ""
for palavra in palavras:     
    if len(palavra) > 2:
        nova_palavra = palavra[0]
        letras = list(palavra[1:len(palavra) - 1])
        random.shuffle(letras)
        for letra in letras:
            nova_palavra += letra
        nova_palavra += palavra[-1] + " "
    else:
        nova_palavra = palavra + " "

    print(f"{palavra} -- {nova_palavra}")
    saida += nova_palavra

print(saida)