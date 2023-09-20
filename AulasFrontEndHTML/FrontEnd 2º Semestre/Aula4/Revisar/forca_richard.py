#importa a biiblioteca random
import random 

#função que irá gerar a forca e o boneco sempre que chamada
def boneco():
    #match que verifica quantas vidas o player tem para printar a forca correta
    match vidas:
            case 6:
                print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
            case 5:
                print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
            case 4:
                print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
            case 3:
                print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
            case 2:
                print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
            case 1:
                print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
            #caso o nr de vidas chegue a 0 irá printar a forca com o boneco completo e a mensagem de derrota
            case 0: 
                print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

### Você Perdeu :( ###\n''')

#lista de palavras válidas que serão sorteadas para adivinhção no código    
#list_p = ['pokemon', 'alienigena', 'carrossel', 'arquitetura', 'aviao', 'caixao', 'cartola', 'metaverso', 'shrek', 'historia']
list_p = ['anel']
#lista que armazena as tentativas do player
list_l = []

#definição de quantas "vidas"(chances) o player tem, qual será a palavra sorteada para adivinhação e o flag que controla a vitoria do player
vidas = 6
sorteio = random.choice(list_p)
ganhou = False

#prints que inserem o menu inicial do jogo, a forca e e listagem de letras
print('''\n#### Jogo da Forca ####
Regras:
- Digite uma letra de cada vez
- Não ́e permitido repetir letras
- Se você acertar, a letra e revelada
- Se errar, perde uma vida
- Você tem 6 vidas
Boa sorte!''')
boneco()
print('_' * len(sorteio))
print()

#inicio do programa utilizando a quantia de vidas como uma condicional para a execução em loop
while vidas > 0:
    #if que define se o loop continua 
    if ganhou == False:
        tamanho = 0
        #a variável tamanho será utilizada para armazenar o tamanho da str inserida
        while tamanho != 1:
            letra = input('Digite uma letra: ').lower()
            tamanho = len(letra)
            #funções para verificação de strings
            #if para verificar se a letra é de fato uma letra 
            if letra.isalpha():
                #caso seja inserido mais de uma letra por vez, o if a seguir identifica e aponta erro, voltando para o laço        
                if tamanho > 1:
                    print('Valor inválido! É permitido digitar apenas 1 letra por vez!')
                #caso seja inserido um única letra, os if a seguir identificam se a mesma já foi selecionada anteriormente      
                else:
                    if letra in list_l:
                        print('Esta letra já foi escolhida anteriormente!')
                        tamanho = 0
                    else:
                        list_l.append(letra)
            #if que verifica se a str é um número                    
            elif letra.isnumeric():
                print('Valor inválido! Não são permitidos números!')
                tamanho = 0   
            #if que verifica se a str é um espaço longo ou se nenhum valor foi digitado
            elif letra.isprintable():
                print('Valor inválido! Você não digitou nenhuma letra!')
                tamanho = 0    
            #if que verifica se a str é um espaço em branco
            elif letra.isspace():
                print('Valor inválido! Você não digitou nenhuma letra!')        
                tamanho = 0
        
        #if que busca a letra digitada dentro da palavra sorteada
        if letra not in sorteio:
            #caso a letra não seja encontrada o player perderá uma vida
            vidas -= 1
            #if que printa quantas vidas o player ainda tem
            if vidas > 2:
                print(f'ERRO! Vidas Restantes: {vidas}')
            elif vidas <= 2:
                print(f'Uhhh!!! Vidas Restantes: {vidas}')
            #função sendo chamada para printa a forca conforme número de vidas atual 
            boneco()
        else:
            #caso a letra seja encontrada, os a letras ainda não descobertas ficarão como '_' e as descobertas aparecerão (a forca também é printada)
            print('Acertou!!!')
            boneco()
            for l in sorteio:
                if l in list_l:
                    print(l, end='')
                else:
                    print('_', end='')
            print('\n')
        
        #flag recebendo "True" para sair do if condicional
        ganhou = True

        #for e if que controlam se todas as letras da palvra sorteada foram digitadas corretamente, aso negativo, envia "False" para ganhou e o loop poder seguir
        for l in sorteio:            
            if l not in list_l:
                ganhou = False
    #caso todas as letras tenham sido devidamente preenchidas, o programa é encerrado 
    else:
        print('### Você ganhou :) ###')
        break    

        