estados = ["AC", "AL" , "AM", "AP" , "BA" , "CE" , "DF" , "ES" , "GO" , "MA" , "MT" , "MS" , "MG" , "PA", "PB" , "PR" , "PE" , "PI", "RJ" , "RN" , "RS" , "RO", "RR" , "SC" , "SP" , "SE" , "TO" ]
idhs    = [0.71, 0.684, 0.7 , 0.688, 0.691, 0.734, 0.814, 0.771, 0.737, 0.676, 0.736, 0.742, 0.774, 0.69, 0.698, 0.769, 0.719, 0.69, 0.762, 0.728, 0.771, 0.7 , 0.699, 0.803, 0.806, 0.702, 0.731]

op = input(f"Busca por [E]stado ou por [I]DH? ").upper()

if op == "E":
    sigla = input("Informe a sigla do estado: ")
    # Assumindo que o usuário digitou uma sigla válida!
    idh = idhs[estados.index(sigla)]
    print(f"IDH de {sigla} = {idh}")
elif op == "I":
    idh = float(input("Informe o valor do IDH: "))
    # Acesso somente aos índices ímpares
    for i in range(0, len(estados)):
        if idh < idhs[i]:
            print(estados[i])
else:
    print("Opção Inválida!")

