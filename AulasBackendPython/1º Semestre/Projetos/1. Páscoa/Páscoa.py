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
#Variaveis que utilizei de flag. "errort(error tipo)" para quando o tipo for inválido e "errorq(error quantia)" para quando a quantia for inválida.
errort = False
errorq = False

#input solicitando o tipo do produto, aceitando tanto caracteres maísuculos ou minúsculos graças ao ".upper".
tipo = input(f'Escolha o tipo de ovo que deseja comprar (A p/ Simples, B p/ Recheado, C p/ Com Surpresa): ').upper()

#if verifica se o tipo do produto é válido e solicita a quantia, do contrário, não faz sentido solicitar a quantidade e parte diretamente para o else.    
if tipo == 'A' or tipo == 'B' or tipo == 'C':
    quantia = int(input('Informe a quantidade desejada: '))

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
#Caso o tipo do produto seja inválido, flega como erro.
else:
    errort = True

#Verifica os flags, caso um dos dois seja verdadeiro, apresenta a mensagem referente ao erro.
if errort != False or errorq != False:
    if errorq:
        print('Quantidade inválida!\nTente novamente digitando um valor positivo para poder efetuar a compra.')
    if errort:
        print('Produto inválido!\nTente novamente escolhendo o produto desejado entre os códigos de A, B ou C')
#Vale notar que ambos os erros nunca aparecerão em conjunto pois se caso o tipo do produto sejá inválido, automáticamente já ignora a solicitação da quantia e apresenta a mensagem de "errort".

#Caso tudo funcione corretamente e o user insira valores válidos, gerá a mensagem de agradecimento/encerramento do programa.
else:
    print('Obrigado por sua compra e Feliz Páscoa!')