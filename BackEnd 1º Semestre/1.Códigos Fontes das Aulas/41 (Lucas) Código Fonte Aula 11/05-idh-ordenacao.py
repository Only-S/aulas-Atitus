estados_idh = {"RN": 0.728,
               "RS": 0.771,
               "RO": 0.7,
               "RR": 0.699,
               "SC": 0.803,
               "BA": 0.691,
               "CE":  0.734,
               "DF":  0.814,
               "PA": 0.69,
               "PB": 0.698,
               "PR": 0.769,
               "PE": 0.719,
               "PI": 0.69,
               "RJ": 0.762,
               "ES":  0.771,
               "GO":  0.737,
               "MA": 0.676,
               "MT": 0.736,
               "AC": 0.71, 
               "AL": 0.684, 
               "AM": 0.7,
               "AP": 0.688,
               "MS": 0.742,
               "SP": 0.806,
               "SE": 0.702, 
               "TO": 0.731,
               "MG": 0.774}

op = input(f"Listar ordenado por [E]stado ou por [I]DH? ").upper()
inverter = input(f"Ordem reversa (sim ou não)? ").lower() == "sim"

if op == "E":
    for estado in sorted(estados_idh, reverse=inverter):
        print(f"{estado}: {estados_idh[estado]}")
elif op == "I":
    for estado in sorted(estados_idh, key=estados_idh.get, reverse=inverter):
        print(f"{estado}: {estados_idh[estado]}")
else:
    print("Opção Inválida!")
