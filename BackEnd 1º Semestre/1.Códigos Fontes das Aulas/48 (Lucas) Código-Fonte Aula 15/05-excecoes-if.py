import sys

val1 = input("Valor 1: ")
val2 = input("Valor 2: ")

if val1.isdigit():
    val1 = int(val1)
else:
    print("val1 é inválido!")
    sys.exit()


if val2.isdigit():
    val2 = int(val2)
else:
    print("val2 é inválido!")
    sys.exit()

if val2 != 0:
    result = val1 / val2
    print(f"Reultado = {result}")
else:
    print("Denominador não pode ser zero!")