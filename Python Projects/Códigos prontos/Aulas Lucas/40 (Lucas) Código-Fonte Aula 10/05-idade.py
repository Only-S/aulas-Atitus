import datetime

# Lê o aniversário do usuário
data = input("Informe seu aniversário (dd/mm/aaaa): ")
dia, mes, ano = data.split("/")
dia, mes, ano = int(dia), int(mes), int(ano)

# Obtém o dia atual
hoje = str(datetime.date.today())
hoje_a, hoje_m, hoje_d = hoje.split("-")
hoje_a, hoje_m, hoje_d = int(hoje_a), int(hoje_m), int(hoje_d)

# Converte as datas para dias
dias_nasc = dia + mes * 30 + ano * 365
dias_hoje = hoje_d + hoje_m * 30 + hoje_a * 365
dias = dias_hoje - dias_nasc

print(f"Você já viveu {dias} dias")

anos = dias // 365
dias = dias % 365
meses = dias // 30
dias = dias % 30

print(f"Você possui {anos} anos, {meses} meses e {dias} dias")