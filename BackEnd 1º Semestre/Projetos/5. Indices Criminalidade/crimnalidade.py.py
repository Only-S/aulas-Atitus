''' Programa que lê arquivos csv contendo indicadores brutos de criminalidade no estado do RS no mês de Janeiro dos anos 2021, 2022 e 2023. 
    Através de um sistema de pontuação de leve até grave, tem como finalidade apresentar o indice total de crimes violentos e não violentos em cada ano, 
    além disso, visa apresetnar um ranking com os cidades com maiores e menores indices de crimes violentos e não violentos, finalizando com a geração'''

#Importação das bibliotecas json e csv
import json
import csv
import calculo_indices_globais
import calculo_indices_cidade

FORMATACAO = 50

def ranking(ciedades_rank, num, crescente, violento):
    print()
    if crescente:
        rank = sorted(ciedades_rank, key=ciedades_rank.get)
        if violento:
            print("-" * FORMATACAO)
            print(f"Top {num} cidades com menor indice de crimes violentos")
            print("-" * FORMATACAO)
        else:
            print("-" * FORMATACAO)
            print(f"Top {num} cidades com menor indice de crimes não violentos")
            print("-" * FORMATACAO)
    else:
        rank = sorted(ciedades_rank, key=ciedades_rank.get, reverse=True)
        if violento:
            print("-" * FORMATACAO)
            print(f"Top {num} cidades com maior indice de crimes violentos")
            print("-" * FORMATACAO)
        else:
            print("-" * FORMATACAO)
            print(f"Top {num} cidades com maior indice de crimes não violentos")
            print("-" * FORMATACAO)
    
    for i in range(num):
        print(f"{i + 1} - {rank[i]}: {ciedades_rank[rank[i]]}")


def imprime_tela(total_v, total_nv, municipios_v, municipios_nv):
    print('-' * FORMATACAO, end='')
    print('\nIndicadores globais por ano')
    print('-' * FORMATACAO, end='')
    print('\nCrimes violentos')
    for i in total_v:
        print(f'- {i}: {total_v[i]}')
    print('\nCrimes não violentos')
    for i in total_nv:
        print(f'- {i}: {total_nv[i]}')
    print('-' * 50, end='')
    ranking(municipios_v, 20, crescente=False, violento=True)
    ranking(municipios_v, 15, crescente=True, violento=True)
    ranking(municipios_nv, 50, crescente=False, violento=False)
    ranking(municipios_nv, 7, crescente=True, violento=False)

def gera_json(dicionario_violento, dicionario_nao_violento):
    with open("crimes_nao_violentos.json", "w") as arq_nao_violento, open("crimes_violentos.json", "w") as arq_violento:
        json.dump(dicionario_nao_violento, arq_nao_violento, indent=4)
        json.dump(dicionario_violento, arq_violento, indent=4)

try:
    jan21 = list(csv.DictReader(open('jan-21.CSV', 'r', encoding='utf-8'), delimiter=';'))
    jan22 = list(csv.DictReader(open('jan-22.CSV', 'r', encoding='utf-8'), delimiter=';'))
    jan23 = list(csv.DictReader(open('jan-23.CSV', 'r', encoding='utf-8'), delimiter=';'))
except OSError:
    print('Falha ao tentar abrir um dos arquivos')

armazenagem = [jan21, jan22, jan23]
total_v = {}
total_nv = {}
cidades_v = {}
cidades_nv = {}
municipios_v = {}
municipios_nv = {}

for i in armazenagem:
    indicador_violento, indicador_nao_violento = calculo_indices_globais.indicadores(i)
    if i == jan21:
        total_v["2021"] = indicador_violento
        total_nv["2021"] = indicador_nao_violento
    elif i == jan22:
        total_v["2022"] = indicador_violento
        total_nv["2022"] = indicador_nao_violento
    elif i == jan23:
        total_v["2023"] = indicador_violento
        total_nv["2023"] = indicador_nao_violento
    else:
        print('ERROR!')

for i in armazenagem:
    cidades_v, cidades_nv = calculo_indices_cidade.indicadores(i)
    for c in cidades_v:
        if c in municipios_v:
            municipios_v[c] += int(cidades_v[c])
        else:
            municipios_v[c] = int(cidades_v[c])
    for c in cidades_nv:
        if c in municipios_nv:
            municipios_nv[c] += int(cidades_nv[c])
        else:
            municipios_nv[c] = int(cidades_nv[c])

imprime_tela(total_v, total_nv, municipios_v, municipios_nv)

gera_json(municipios_v, municipios_nv)
