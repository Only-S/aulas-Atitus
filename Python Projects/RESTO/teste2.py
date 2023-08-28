import json

def carrega_cidades():
    try:
        with open("paises-estados-cidades.json", "r", encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("O arquivo não foi encontrado!")

def salva_cidades(list_cidades):
    saida = {}
    try:
        for pais in list_cidades:
            nome_pais = pais["name"]
            estados = pais["states"]
            for estado in estados:
                nome_estado = estado["name"]
                cidades = estado["cities"]
                for cidade in cidades:
                    nome_cidade = cidade["name"]
                    if nome_cidade[0].upper() == "A":
                        saida[nome_cidade] = {"pais": nome_pais, "estado": nome_estado}
        with open("cidades_A.json", "w") as arquivo_saida:
            json.dump(saida, arquivo_saida, indent=4)
    except OSError:
        print("Erro ao salvar o as cidades!")

dicionario = carrega_cidades()
salva_cidades(dicionario)

with open("cidades_A.json", 'r', encoding='utf-8') as arq:
    for i in arq:
        print(i)

