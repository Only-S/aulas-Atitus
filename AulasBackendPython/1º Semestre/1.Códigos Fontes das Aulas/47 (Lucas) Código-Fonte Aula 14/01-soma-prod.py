def soma_mult(valor1, valor2):
    soma = valor1 + valor2
    produto = valor1 * valor2
    return soma, produto

## Programa Principal
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

s, p = soma_mult(v1, v2)

print(f"Resultado da soma: {s:.2f}")
print(f"Resultado da produto: {p:.2f}")