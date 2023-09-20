A = True
B = False
C = True

if A:
	if B:
		print("Comando 1")
	else:
		print("Comando 2")
	print("Comando 3")
else:
	print("Comando 4")
	if C:
		print("Comando 5")
	elif B:	
		print("Comando 6")
		
'''
Quais comandos serão executados se:
a) A = True, B = False e C = True - 2 e 3
b) A = False, B = True e C = True - 4 e 5 
c) A = True, B = True e C = False - 1 e 3 
d) A = False, B = False e C = False - 4 
e) Quais os valores de A, B e C para que somente os comandos 4 e 6 sejam executados? - False, True, False
'''