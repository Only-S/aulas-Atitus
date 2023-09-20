import json

def grava(contas):
    with open("contas.json", 'w', encoding="utf-8") as arquivo:
        json.dump(contas, arquivo)

def carregar():
    try:
        with open("contas.json", 'r', encoding="utf-8") as arquivo:
            contas = json.load(arquivo)
            return contas
    except FileNotFoundError:
        return []