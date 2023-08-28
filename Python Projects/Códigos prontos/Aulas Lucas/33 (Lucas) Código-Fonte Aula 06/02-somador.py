'''
Soma as despesas de uma pessoa até que seja informado o valor zero.
'''

despesas = 0
valor = 1
while valor != 0:
    valor = float(input("Informe a despesa (0 p/ sair): "))
    despesas += valor

print(f"Total Despesas: R${despesas:.2f}")


