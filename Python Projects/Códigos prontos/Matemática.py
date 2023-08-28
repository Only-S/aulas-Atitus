#Uso de Mod e Div - Exemplo (dúvidas consultar - Aula 02 -)
din = int(input("Informe o valor que deseja sacar: "))
print("\n")
print("Valor lido: R$", din)
res = din // 100
print(f"Você recebéra {res} notas de R$100,00 ")
din = din % 100
res = din // 50
print(f"{res} notas de R$50,00")
din = din % 50
res = din // 20
print(f"{res} notas de R$20,00")
din = din % 20
res = din // 10
print(f"{res} notas de R$10,00")
din = din % 10
res = din // 5
print(f"{res} notas de R$5,00")
din = din % 5
res = din // 2
print(f"{res} notas de R$2,00")
din = din % 2
print(f"{din} notas de R$1,00")
print()

#Trigonometria - Exemplo (dúvidas consultar - Aula 02 -)
import math
angulo = float(input("Informe o ângulo da escada com o chão (em graus): "))
parede = float(input("Informe a altura da parede (em metros): "))
# Converte o ângulo para radianos
radianos = angulo * math.pi / 180
escada = parede / math.sin(radianos)
print(f"A altura da escada é de {escada:.2f} metros")

#Pares num Intervalo
inicio, fim = input("Informe o início e o fim do intervalo: ").split(" ")
inicio, fim = int(inicio), int(fim)
if inicio % 2 != 0: # Garante que o primeiro valor do intervalo é par
    inicio += 1
for i in range(inicio, fim + 1, 2):
    print(f"{i} ", end="")

#Fatorial - Exemplo (dúvidas consultar - Aula 05 -)
n = int(input("Informe um número positivo: "))

fat = 1
for i in range(1, n + 1):
    fat = fat * i

print(f"FAT = {fat}")

#Fibonnaci - Exemplo (dúvidas consultar - Aula 05 -)
pos = int(input("Entre com o termo desejado: "))
if pos < 0:
    print("A posição não pode ser negativa!")
else:
    if pos == 0:
        fib = 0
    elif pos == 1:
        fib = 1
    else:
        t_2 = 0
        t_1 = 1
        for i in range(2, pos + 1):
            fib = t_2 + t_1
            t_2 = t_1
            t_1 = fib
print(f"O termo {pos} da série de Fibonacci é {fib}")