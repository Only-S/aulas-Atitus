import sys

try:
    val1 = int(input("Valor 1: "))
    val2 = int(input("Valor 2: "))

    result = val1 / val2
    print(f"Reultado = {result}")

except ValueError:
    print("O valor informado é inválido!")
    sys.exit()
except ZeroDivisionError:
    print("Denominador não pode ser zero!")
