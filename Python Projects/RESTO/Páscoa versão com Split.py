'''
Programa que processa uma venda de ovos de páscoa e avisa caso o TIPO inserido seja inválido ou a QUANTIA desejada seja excedente ou inválida. Caso a inserção de informações pelo usuário ocorra corretamente, o programa apresenta quantos ovos de determinado tipo o cliente selecionou e qual o preço em R$ que irá pagar.
'''
import math
#Constantes de Preço e Limite para ovos do tipo Simples.
A = 12.00
LA = 50
#Constantes de Preço e Limite para ovos do tipo Recheado.
B = 15.50
LB = 30
#Constantes de Preço e Limite para ovos do tipo Com Surpresa.
C = 21.30
LC = 20

#Início do programa
#Variaveis que utilizei de flag. "errort" para quando o tipo for inválido e "errorq" para quando a quantia for inválida.
errort = False
errorq = False

#Input solicitando o tipo e quantia do produto em conjunto separados por "(espaço)" graças ao ".split", aceitando tanto caracteres maísuculos ou minúsculos graças ao ".upper".
tipo, quantia = input(f'Escolha o tipo de ovo (A p/ Simples, B p/ Recheado, C p/ Com Surpresa) e a quantidade que deseja comprar: ').upper().split()
#Definição da variável "quantia" como int, pois caso não o faça o programa a interpretará como uma string.
quantia = int(quantia)

#match busca em 'tipo' qual das opções foi selecionada, como o erro de caracteres fora do escopo foi tratado anteriormente, não se faz necessário um "case_:" aqui.        
match tipo:    
    case 'A':
        #if testando se a quantia inserida está dentro do Limite estipulado para o produto.
        if quantia > 0 and quantia <= LA:
            pgto = A * quantia
            print(f'Você solicitou {quantia} ovos do tipo Simples no valor total de R$ {pgto:.2f}.')
        #elif testando se excede o limite.
        elif quantia > LA:
            pgto = A * LA
            print('Limite excedido.')
            print(f'Você comprará {LA} ovos do tipo Simples no valor total de R$ {pgto:.2f}.')
        #Caso o valor inserido em "quantia" seja um valor negativo, flega como erro.
        else:            
            errorq = True
    #O precesso se repete para os demais cases.        
    case 'B':
        if quantia > 0 and quantia <= LB:
            pgto = B * quantia
            print(f'Você solicitou {quantia} ovos do tipo Recheado no valor total de R$ {pgto:.2f}.')
        elif quantia > LB:
            pgto = B * LB
            print('Limite excedido.')
            print(f'Você comprará {LB} ovos do tipo Recheado no valor total de R$ {pgto:.2f}.')
        else:            
            errorq = True
    case 'C':
        if quantia > 0 and quantia <= LC:
            pgto = C * quantia
            print(f'Você solicitou {quantia} ovos do tipo Com Surpresa no valor total de R$ {pgto:.2f}.')
        elif quantia > LC:
            pgto = C * LC
            print('Limite excedido.')
            print(f'Você comprará {LC} ovos do tipo Com Surpresa no valor total de R$ {pgto:.2f}')
        else:            
            errorq = True
    #Caso o tipo do produto seja inválido, flega como erro e em seguida também verifica se a quantia também é um valor inválido.        
    case _:
        errort = True
        if quantia < 0:
            errorq = True

#Verifica os flags e tenta desccobrir se ambos são verdadeiros ou apenas um deles e em seguida apresenta a mensagem referente.
if errort != False or errorq != False:
    if errort == errorq:
        print('Produto e quantidade inválidos! Tente novamente escolhendo o produto desejado entre os códigos de A, B ou C e uma quantia positiva.')
        #Mensagem única caso ambos o erros seja verdadeiros.
    else:
    #Mensagens destinadas a cada erro em caso de um só ser verdadeiro.
        if errorq:
            print('Quantidade inválida!\nTente novamente digitando um valor positivo para poder efetuar a compra.')
        if errort:
            print('Produto inválido!\nTente novamente escolhendo o produto desejado entre os códigos de A, B ou C')

#Caso tudo funcione corretamente e o user insira valores válidos, gerá a mensagem de agradecimento/encerramento do programa.
else:
    print('Obrigado por sua compra e Feliz Páscoa!')