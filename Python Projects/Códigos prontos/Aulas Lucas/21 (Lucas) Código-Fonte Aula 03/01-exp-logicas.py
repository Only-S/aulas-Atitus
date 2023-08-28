'''
Programa que exemplifica a utilização de expressões lógicas em Python
'''

a = 1
b = 3
c = 5
d = 7
valor = 9

e1 = (a > b) or (c < d)
e2 = valor > 10
e3 = not (a + c < b)
e4 = (a == b)
e5 = (a == b) and (a >= c)
e6 = (a != b)
e7 = not ((a >=b) or (a < c))

print(e1, e2, e3, e4, e5, e6, e7)