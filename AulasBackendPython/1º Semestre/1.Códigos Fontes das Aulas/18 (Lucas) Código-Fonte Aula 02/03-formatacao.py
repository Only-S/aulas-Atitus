'''
Programa que testa diversos formatadores para os tipos primitivos
'''

## Formatação de float

valor = 8.29563

print(f"{valor:6.2f}")

# Testando outras formatações
valor = 99.7567892
print(f"Valor com 9f   = [{valor:9f}]")
print(f"Valor com 9.0f = [{valor:9.0f}]")
print(f"Valor com 9.1f = [{valor:9.1f}]")
print(f"Valor com 9.2f = [{valor:9.2f}]")
print(f"Valor com 9.3f = [{valor:9.3f}]")
print(f"Valor com 1.2f = [{valor:1.2f}]")

## Formatação de string

nome = "Maria"

print(f"[{nome}]")
print(f"[{nome:10}]")
print(f"[{nome:>20}]")
print(f"[{nome:^50}]")

# Formatação de inteiros

num = 1234

print(f"[{num:2}]")
print(f"[{num:6}]")
print(f"[{num:08}]")