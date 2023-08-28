import csv

with open("video-games.csv", "r", encoding="utf-8") as entrada, open("jogos-pc.csv", "w", encoding="utf-8", newline="") as saida:
    csv_reader = csv.DictReader(entrada, delimiter=",")
    cabecalho = ["Rank", "Titulo", "Lancamento"]
    csv_writer = csv.DictWriter(saida, delimiter="\t", fieldnames=cabecalho)
    csv_writer.writeheader()
    for linha in csv_reader:
        if linha['Platform'] == "PC":
            dados = {
                "Rank" : linha['Rank'],
                "Titulo" : linha['Name'],
                "Lancamento" : linha['Date']
            }
            csv_writer.writerow(dados)