texto = '''Alan Mathison Turing (Londres, 23 de junho de 1912 — Wilmslow, Cheshire, 7 de junho de 1954) foi um matemático, cientista da computação, lógico, criptoanalista, filósofo e biólogo teórico britânico. Turing foi altamente influente no desenvolvimento da moderna ciência da computação teórica, proporcionando uma formalização dos conceitos de algoritmo e computação com a máquina de Turing, que pode ser considerada um modelo de um computador de uso geral.Ele é amplamente considerado o pai da ciência da computação teórica e da inteligência artificial. Apesar dessas realizações ele nunca foi totalmente reconhecido em seu país de origem durante sua vida por ser homossexual e porque grande parte de seu trabalho foi coberto pela Lei de Segredos Oficiais.
'''

busca = input("Informe o texto a ser buscado: ")
ini = int(input("Informe a posição de início: "))
fim = int(input("Informe a posição final: "))

pos = texto.find(busca, ini, fim)

if pos != -1:
    print(f"Substring {busca} encontrada em {pos}: [{texto[pos-10:pos+len(busca)+10]}]")
else:
    print("Valor não encontrado!")