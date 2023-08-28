import csv

with open('video-games.csv', 'r', encoding='utf-8') as arquivo, open("new-games.csv", "w", encoding='utf-8', newline='') as arq:
    csv_reader = csv.DictReader(arquivo, delimiter=',')
    cabecalho = ["Rank", "Titulo", "Lancamento"]
    csv_writer = csv.DictWriter(arq, delimiter='\t', fieldnames=cabecalho)
    csv_writer.writeheader()
    for linha in csv_reader:
        if linha['Platform'] == "PC":
            dados = {
                "Rank" : linha['Rank'],
                "Titulo" : linha['Name'],
                "Lancamento" : linha['Date']
            }
            csv_writer.writerow(dados)




