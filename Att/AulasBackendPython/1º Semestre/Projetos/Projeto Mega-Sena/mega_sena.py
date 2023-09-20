import csv

def ler_dados(dicionario):
    try:
        with open("mega_sena.csv", "r", encoding="utf8") as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            cabecalho = next(leitor)
            for linha in leitor:
                dicionario[linha[0]] = list(linha[2:])
    except OSError:
        print("Falha ao tentar abrir o arquivo")
    return dicionario


def conta_frequencia(dados, numero, bola = -1):
    soma = 0
    maior = 0
    if bola < 0:
        for chave in dados.values():
            for valores in chave:
                if int(valores) == numero:
                    soma += 1
        return soma
    elif bola > 6:
        print("Só são sorteada 6 bolas pra cada número!")
    else:        
        for chave in dados.values():
            if int(chave[bola]) == numero:
                soma += 1
        return soma   

def relatorio_frequencia(dados):
    numero = 1    
    contagem = 0
    contagem_menor = 999999999999999999999999
    with open("relatorio.txt", "w", encoding="utf8") as arq:
        while numero <= 60:
            total = conta_frequencia(dados, numero)        
            if total > contagem:
                contagem = total
                salva_maior = numero
            if total < contagem_menor:
                contagem_menor = total
                salva_menor = numero
            arq.write(f"Numero {numero}:\n\tFrequência Geral:{total}\n\tFrequência por posição:\n")
            for bola in range(6):
                controlepos = conta_frequencia(dados, numero, bola)
                arq.write(f"\t\tPosição {bola+1}: {controlepos}\n")             
            numero += 1

    print(f"O maior número é o {salva_maior} que foi sorteado um total de {contagem} vezes")
    print(f"O maior número é o {salva_menor} que foi sorteado um total de {contagem_menor} vezes") 

dados = {}

dados = ler_dados(dados)

relatorio_frequencia(dados)