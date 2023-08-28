'''
Programa que pega dados de crimes ocorridos no estado em janeiro de 2021, 2022 e 2023 que estão armazenados em três arquivos .csv (planilhas) e então estipula um sistema de pontuação para gerar um indice de criminalidade e rankear as cidades com mais crimes violentos e não violentos do estado, além de gerar um arquivo .json com todos os indices de crimes violentos e não violentos do estado somando os 3 anos
'''


def calcula_indices_totais(): #Função que gera os indices de crimes totais de cada ano

    try:
        with open("jan-21.CSV", "r", encoding="utf-8") as arq_21, open("jan-22.CSV", "r", encoding="utf-8") as arq_22, open("jan-23.CSV", "r", encoding="utf-8") as arq_23:
            lista_tabelas = [arq_21, arq_22, arq_23] #Após abrir os 3 arquivos eu armazeno eles em uma lista para poder percorre-la
            
            crimes_violentos = {} #Dicionário que armazenará o indice de crimes violentos
            crimes_nao_violentos = {} #Dicionário que armazenará o indice de crimes não violentos

            indice_violento = 0  
            indice_nao_violento = 0 
            for tabela in lista_tabelas: #Um laço que percorerá a lista com os arquivos
                leitor = csv.DictReader(tabela, delimiter=";")
                for linha in leitor:
                    if linha["Municipios"] == "ACEGUA": #Verificando se o município sendo analisado é o primeiro da tabela
                        if indice_violento > 0 and indice_nao_violento > 0: #Se ele for o primeiro elemento e tiver com os contadores maiores que zero os valores serão zerados para poder separar o número respectivo de cada ano
                            indice_violento = 0
                            indice_nao_violento = 0
                            #Parte do código que multiplica todos os crimes por seus respectivos pontos e guarda o resultado em uma variável:
                            indice_violento += int(linha["Vitimas de Homicidio Doloso"]) * 10 + int(linha[" Roubos"]) * 2 + int(linha[" Roubo de Veiculo"]) * 3 + int(linha[" Delitos Relacionados a Armas e Municoes"]) * 2 + int(linha[" Entorpecentes Trafico"]) * 5 + int(linha["Vitimas de Latrocinio"]) * 10 + int(linha["Vitimas de Lesao Corp Seg Morte"]) * 10
                            indice_nao_violento += int(linha[" Furtos"]) * 3 + int(linha["Furto de Veiculo "]) * 3 + int(linha[" Estelionato"]) * 1 + int(linha[" Entorpecentes Posse"]) * 2
                        else:
                            indice_violento += int(linha["Vitimas de Homicidio Doloso"]) * 10 + int(linha[" Roubos"]) * 2 + int(linha[" Roubo de Veiculo"]) * 3 + int(linha[" Delitos Relacionados a Armas e Municoes"]) * 2 + int(linha[" Entorpecentes Trafico"]) * 5 + int(linha["Vitimas de Latrocinio"]) * 10 + int(linha["Vitimas de Lesao Corp Seg Morte"]) * 10
                            indice_nao_violento += int(linha[" Furtos"]) * 3 + int(linha["Furto de Veiculo "]) * 3 + int(linha[" Estelionato"]) * 1 + int(linha[" Entorpecentes Posse"]) * 2   
                    else:
                        indice_violento += int(linha["Vitimas de Homicidio Doloso"]) * 10 + int(linha[" Roubos"]) * 2 + int(linha[" Roubo de Veiculo"]) * 3 + int(linha[" Delitos Relacionados a Armas e Municoes"]) * 2 + int(linha[" Entorpecentes Trafico"]) * 5 + int(linha["Vitimas de Latrocinio"]) * 10 + int(linha["Vitimas de Lesao Corp Seg Morte"]) * 10
                        indice_nao_violento += int(linha[" Furtos"]) * 3 + int(linha["Furto de Veiculo "]) * 3 + int(linha[" Estelionato"]) * 1 + int(linha[" Entorpecentes Posse"]) * 2

                    #Sessão do código que verifica qual arquivo está sendo lido e então guarda o valor dos incies na key do seu respectivo ano
                    if tabela == arq_21:
                        crimes_violentos["2021"] = indice_violento
                        crimes_nao_violentos["2021"] = indice_nao_violento
                    elif tabela == arq_22:
                        crimes_violentos["2022"] = indice_violento
                        crimes_nao_violentos["2022"] = indice_nao_violento
                    elif tabela == arq_23:
                        crimes_violentos["2023"] = indice_violento
                        crimes_nao_violentos["2023"] = indice_nao_violento

            return crimes_violentos, crimes_nao_violentos #Retornando os 2 dicionários criados
    except OSError:
        print("Ocorreu um erro ao tentar abrir o arquivo!!")

def calcula_indices_cidades(): #Função que calcula os indices e guarda eles em seus respectivos municipios

    try:
        with open("jan-21.CSV", "r", encoding="utf-8") as arq_21, open("jan-22.CSV", "r", encoding="utf-8") as arq_22, open("jan-23.CSV", "r", encoding="utf-8") as arq_23:
            lista_tabelas = [arq_21, arq_22, arq_23]
            
            indices_cidades_violentas = {}
            indices_cidades_nao_violentas = {}

            for arquivo in lista_tabelas:
                leitor = csv.DictReader(arquivo, delimiter=";")
                for linha in leitor:
                    indice_violento = 0
                    indice_nao_violento = 0
                    municipio = linha["Municipios"]
                    indice_violento += int(linha["Vitimas de Homicidio Doloso"]) * 10 + int(linha[" Roubos"]) * 2 + int(linha[" Roubo de Veiculo"]) * 3 + int(linha[" Delitos Relacionados a Armas e Municoes"]) * 2 + int(linha[" Entorpecentes Trafico"]) * 5 + int(linha["Vitimas de Latrocinio"]) * 10 + int(linha["Vitimas de Lesao Corp Seg Morte"]) * 10
                    indice_nao_violento += int(linha[" Furtos"]) * 3 + int(linha["Furto de Veiculo "]) * 3 + int(linha[" Estelionato"]) * 1 + int(linha[" Entorpecentes Posse"]) * 2

                    if municipio in indices_cidades_violentas:
                        indices_cidades_violentas[municipio] = indices_cidades_violentas[municipio] + indice_violento #Se o municipio que está sendo lido já estiver no dicionário significa que estamos em outro ano, então ele somará o valor antigo com o a recém gerado
                    else:
                        indices_cidades_violentas[municipio] = indice_violento #Senão ele apenas irá inserir o valor gerado no cálculo
                        
                    if municipio in indices_cidades_nao_violentas: #O mesmo se repete para os crimes não violentos
                        indices_cidades_nao_violentas[municipio] = indices_cidades_nao_violentas[municipio] + indice_nao_violento
                    else:
                        indices_cidades_nao_violentas[municipio] = indice_nao_violento
        
            return indices_cidades_violentas, indices_cidades_nao_violentas
    except:
        print("Ocorreu um erro ao tentar abrir o arquivo!!")

def ranking(dicionario, num, crescente=True, violento=True): #Função que gera o ranking e recebe como parâmetro o dicionário que será rankeado, o número de posições, se será em ordem crescente ou não e se será analisado crimes violentos ou não violentos

    TRACOS = 60 #Constante que gerencia o número de traços na exibição dos rankings
    print()
    if crescente:
        rank = sorted(dicionario, key=dicionario.get) #Se a ordem for crescente o dicionário será organizado pelos valores das keys em ordem do menor até o maior e gera uma lista com as keys na posição em ordem
        if violento:
            print("-" * TRACOS)
            print(f"Top {num} cidades com menor indice de crimes violentos") #Se for um ranking de crimes violentos ele irá imprimir o enunciado de acordo com os parâmetros inseridos
            print("-" * TRACOS)
        else:
            print("-" * TRACOS)
            print(f"Top {num} cidades com menor indice de crimes não violentos") #A mesma coisa para caso for crimes não violentos
            print("-" * TRACOS)
    else:
        rank = sorted(dicionario, key=dicionario.get, reverse=True) #Se crescente for False ele irá ordenar o dicionário de forma reversa, do maior para o menor
        if violento:
            print("-" * TRACOS)
            print(f"Top {num} cidades com maior indice de crimes violentos")
            print("-" * TRACOS)
        else:
            print("-" * TRACOS)
            print(f"Top {num} cidades com maior indice de crimes não violentos")
            print("-" * TRACOS)
    
    for i in range(num):
        print(f"{i + 1} - {rank[i]}: {dicionario[rank[i]]}") #Aqui será printado o número de posições imprimindo a key que está na lista rank e o valor respectivo no dicionário original

def exibicao(total_crimes_violentos, total_crimes_nao_violentos, cidades_violentas, cidades_nao_violentas): #Função que irá exibir todas as informações do programa e recebe como parâmetro todos os dicionários usados, 2 com os valores totais e 2 com os valores por municipios

    TRACOS = 40
    print("-" * TRACOS)
    print("Indicadores globais por ano")
    print("-" * TRACOS)
    print("Crimes violentos")
    print(f"- 2021: {total_crimes_violentos['2021']} \n- 2022: {total_crimes_violentos['2022']} \n- 2023: {total_crimes_violentos['2023']}")
    print("Crimes não violentos")
    print(f"- 2021: {total_crimes_nao_violentos['2021']} \n- 2022: {total_crimes_nao_violentos['2022']} \n- 2023: {total_crimes_nao_violentos['2023']}")
    print("-" * TRACOS)
    ranking(cidades_violentas, 20, crescente=False, violento=True)
    ranking(cidades_violentas, 15, crescente=True, violento=True)
    ranking(cidades_nao_violentas, 50, crescente=False, violento=False)
    ranking(cidades_nao_violentas, 7, crescente=True, violento=False)

def escreve_arquivo(dicionario_violento, dicionario_nao_violento): #Função que irá escrever em um arquivo json os dois dicionários com os indices de crimes violentos e não violentos de cada municipio nos 3 anos
    with open("crimes_nao_violentos.json", "w") as arq_nao_violento, open("crimes_violentos.json", "w") as arq_violento:
        json.dump(dicionario_nao_violento, arq_nao_violento, indent=4) #Usando o dump e a identação para transferir as keys e os valores do dicionário para o arquivo json
        json.dump(dicionario_violento, arq_violento, indent=4)

#----------------------------------MAIN----------------------------------

#Importando as bibliotecas csv e json
import csv 
import json

#Atribuindo as funções de calculo em seus respectivos dicionários:
indice_crimes_violentos, indice_crimes_nao_violentos = calcula_indices_totais()
cidades_violentas, cidades_nao_violentas = calcula_indices_cidades()

exibicao(indice_crimes_violentos, indice_crimes_nao_violentos, cidades_violentas, cidades_nao_violentas) #Chamando a função de exibição usando os dicionários criados acima como parâmetro

escreve_arquivo(cidades_violentas, cidades_nao_violentas) #Invocando a função que escreverá o arquivo json com os dicionários dos municipios como parâmetro