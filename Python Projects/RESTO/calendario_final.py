'''
Programa que irá exibir um calendário de maneira visual de acordo com as medidas informadas pelo usuário

'''

tamanho = int(input("Insira a quantidade de dias no mês: ")) #Essa variável é a responsável por guardar quantos dias terá no mês indicado

while tamanho < 28 or tamanho > 31: #Aqui é feita uma verificação, só são válidos meses com 28 a 31 dias (29 conta por causa dos anos bissextos)
    tamanho = int(input("VALOR INVÁLIDO! Insira a quantidade de dias no mês (28/31): "))

dia = int(input("Insira em qual dia da semana o mês iniciará (1 = DOM, 2 = SEG...): ")) #Essa variável é a responsável por guardar o dia inicial do mês (se começa no domingo, segunda, terça...)

while dia < 1 or dia > 7: #Fazendo uma verificação na variável "dia" como a semana só tem 7 dias só serão aceitos valores nessa janela
    dia = int(input("VALOR INVÁLIDO! Insira em qual dia da semana o mês iniciará (1 = DOM, 2 = SEG...): "))

print("DOM SEG TER QUA QUI SEX SAB") #Exibição da parte superior do calendário com os dias da semana

print("    " * (dia-1), end="") #Com esse comando eu imprimo os espaços nos casos do mês iniciar no meio da semana, sendo necessário preencher os dias anteriores como vazio

for i in range (1, tamanho + 1): #Laço de repetição responsável por imprimir todos os dias do 1 até o "tamanho" informado pelo usuário
    print(f"{i:02}", end = "  ")
    dia = dia + 1
    if dia > 7: #Aqui eu utilizo um contador reaproveitando do input do usuário na varíavel "dia" para definir que sempre ao chegar no sétimo dia da semana irá ocorrer uma quebra de linha
        print()
        dia = 1