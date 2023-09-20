'''
Exemplos de como formatar a saída em Python
'''

nome = "Lucas"
matricula = 305016
nota = 9.7539

# Saída de variáveis normal
print("Aluno:", nome, "(", matricula, ") - Nota:", nota)

# Saída com printf-style
print("Aluno: %s (%d) - Nota: %.1f" % (nome, matricula, nota))

# Saída com str.format()
print("Aluno: {} ({}) - Nota: {:.1f}".format(nome, matricula, nota))

print("Aluno: {0} ({1}) - Nota: {2:.1f}".format(nome, matricula, nota)) # uso de índices

print("Aluno: {1} ({2:.1f}) - Nota: {0}".format(nome, matricula, nota)) # índices em outra ordem

# Saída com f-string
print(f"Aluno: {nome} ({matricula}) - Nota: {nota:.1f}")

