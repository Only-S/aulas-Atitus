def funcao1():
    cont = 10   # cont agora pertence ao escopo da funcao1
    for i in range(1, cont):
        print(".", end="")
    print(f"\ncont funcao1 = {cont}")

# Programa Principal
cont = 5    # cont pertence ao escopo principal
print(f"cont principal = {cont}")
funcao1()
print(f"cont principal após funcao1 = {cont}")
funcao1()
print(f"cont principal após funcao1 = {cont}")