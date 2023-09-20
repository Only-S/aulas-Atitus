def imc(peso, altura):
    i = peso / (altura ** 2)
    return i

# Programa Principal
p = float(input("Digite seu peso em Kg: "))
a = float(input("Digite sua altura em m: "))

i = imc(p, a)

print(f"Seu IMC é {i:.2f} - Você está ", end="")
if i < 18.5:
    print("abaixo do peso")
elif i <= 25:
    print("com peso normal")
elif i <= 30:
    print("acima do peso")
else:
    print("obeso")