import json

def carrega_cidades():
    try:
        with open("paises-estados-cidades.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("O arquivo não foi encontrado!")

def salva_cidades(list_cidades):
    try:
        with open("cidades_A.json", "w") as arquivo:
            if list_cidades["name"] == "A":
                    json.dump(list_cidades, arquivo)
    except OSError:
        print("Erro ao salvar o baralho!")

dicionario = carrega_cidades()
print(dicionario)

#salva_cidades(dicionario)

