estados_idh = {"AC": 0.71, 
               "AL": 0.684, 
               "AM": 0.7,
               "AP": 0.688,
               "BA": 0.691,
               "CE":  0.734,
               "DF":  0.814,
               "ES":  0.771,
               "GO":  0.737,
               "MA": 0.676,
               "MT": 0.736,
               "MS": 0.742,
               "MG": 0.774,
               "PA": 0.69,
               "PB": 0.698,
               "PR": 0.769,
               "PE": 0.719,
               "PI": 0.69,
               "RJ": 0.762,
               "RN": 0.728,
               "RS": 0.771,
               "RO": 0.7,
               "RR": 0.699,
               "SC": 0.803,
               "SP": 0.806,
               "SE": 0.702, 
               "TO": 0.731}

op = input(f"Busca por [E]stado ou por [I]DH? ").upper()

if op == "E":
    sigla = input("Informe a sigla do estado: ")
    # Assumindo que a sigla digitada é válida
    print(f"IDH de {sigla} = {estados_idh[sigla]}")
elif op == "I":
    idh = float(input("Informe o valor do IDH: "))
    for estado in estados_idh:
        if idh < estados_idh[estado]:
            print(estado)
else:
    print("Opção Inválida!")