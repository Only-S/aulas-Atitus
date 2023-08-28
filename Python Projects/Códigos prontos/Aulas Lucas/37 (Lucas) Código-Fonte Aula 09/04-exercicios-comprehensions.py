temperaturas = [88, 94, 97, 89, 101, 98, 102, 95, 100]

t1 = [t for t in temperaturas if t >= 100]
print(t1)

t2 = [(t - 32) * 5/9 for t in temperaturas]
print(t2)

'''Produzir uma lista com as consoantes que aparecem em uma variável string chamada palavra'''
palavra = "abacaxi"
consoantes = [letra for letra in palavra if letra not in "aeiou"]
print(consoantes)

'''Criar uma lista dos números entre 1 e 100 que são divisíveis por 3. '''
div3 = [numero for numero in range(1, 101) if numero % 3 == 0]
print(div3)

div3 = [numero for numero in range(3, 101, 3) ]
print(div3)

'''Criar uma lista de números chamada valores_zero, à partir de uma lista de números em ponto flutuante chamada leituras, selecionando somente os valores que estão a uma distância epsilon de zero.'''
leituras = [1.1, -2.4, 6.14, -1.06, 8.3, 2.164, -3.8, 5.0, 7.7]
epsilon = 3.6

valores_zero = [valor for valor in leituras if abs(valor) < epsilon]
print(valores_zero)

