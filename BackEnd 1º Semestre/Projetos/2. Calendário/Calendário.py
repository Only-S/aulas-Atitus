'''
Programa que gera um calendário conforme a quantidade de dias do mês e o dia da semana que ele inicia, a partir de inputs do usuário.
'''

#Definição das variáveis de controle:
#Variável "c" será responsável por quebrar a linha quando o espaço de 7 dias no calendário forem preenchidos.
c = 0
#"j" será utilizada como variável de controle.
j = 1

#Será utilizado para dar os espaçamentos do calendário.
space =''

#Variável "nd" solicita ao usuário o número de dias que terá o mês, não sendo permitido valor menor que 28 ou maior que 31.
nd = int(input('Informe o número de dias do mês: '))
while nd < 28 or nd > 31:
    #Caso um valor inválido seja digitado, entra em laço infinito, até inserção de valor válido.
    nd = int(input('VALOR INVÁLIDO! Informe o numero de dias do mês: '))

#Variável "ds" solicita ao usuário qual dia semana irá iniciar o mês, não sendo permitido valor menor que 1 ou maior que 7.
ds = int(input('Informe o dia da semana: '))
while ds < 1 or ds > 7:
    #Caso um valor inválido seja digitado, entra em laço infinito, até inserção de valor válido.
    ds = int(input('VALOR INVÁLIDO! Informe o dia da semana: '))

#Adiciona uma linha em branco para melhor visualização.
print()

#Cria a linha de dias da semana onde Domingo é o 1º dia e Sábado o 7º.
print('   DOM   SEG   TER   QUA   QUI   SEX   SAB')

#Trecho que de fato gera o calendário:
#O "for" de "i" até "nd" irá escrever os dias de 1 até o número de dias inserido pelo usuário: 28, 29, 30 ou 31.
for i in range(nd):
    #O "while" busca adicionar espaços em branco no calendário para os números serem realocados à direita do calendário.
    while j < ds:
        print(f'{space:^6}', end='')
        j += 1
        #A variável "c" precisa ser incrementada dentro deste laço pois ela é quem vai quebrar a linha e impedir que os valores "vazem" o espaço do calendário.
        c += 1        
    #O print a seguir escreve dia por dia do calendário e adiciona um espaçamento para manter as colunas do calendário alinhadas e centralizadas.
    print(f'{space:^3}{i+1:02d}', end=' ')
    c += 1
    #Eis aqui o "c" realizando sua função de quebrar as linhas que o espaço necessário exceder o equivalente a 7 valores.
    if c > 6:
        print('')
        c = 0
#Os 2 prints sequências apenas adicionam linha em branco para melhor viasualização do calendário.        
print('')
print('')