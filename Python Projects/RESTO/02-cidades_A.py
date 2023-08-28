import json

# Abre o arquivo para leitura
with open("paises-estados-cidades.json", "r", encoding='utf-8') as arquivo:
    dicionario = json.load(arquivo)

saida = {}
for pais in dicionario:
    nome_pais = pais["name"]
    #print(nome_pais)
    estados = pais["states"]
    for estado in estados:
        nome_estado = estado["name"]
        #print("\t", nome_estado)
        cidades = estado["cities"]
        for cidade in cidades:
            nome_cidade = cidade["name"]
            if nome_cidade[0].upper() == "A":
                
                #print("\t\t", nome_cidade)
                saida[nome_cidade] = {
                    "pais": nome_pais,
                    "estado": nome_estado
                }
            
with open("cidades_A.json", "w") as arq_saida:
    json.dump(saida, arq_saida, indent=4)