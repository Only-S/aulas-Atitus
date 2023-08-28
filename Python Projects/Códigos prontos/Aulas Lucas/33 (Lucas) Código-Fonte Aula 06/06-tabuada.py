'''
Programa qie gera a tabuada do 1 até o 10.
ENTRADA: Não há.
SAÍDA  : Impressão da tabuada na tela
'''
for multiplicador in range(1, 11):
    print(f"Tabuada do {multiplicador}")
    for multiplicando in range(1, 11):
        print(f"{multiplicando} x {multiplicador} = {multiplicando * multiplicador}")
    print() # Deixa uma linha em branco