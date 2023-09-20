def criar(arquivo, conta):
    nova_conta = {
        "nome": conta["nome"],
        "email": conta["email"],
        "saldo": conta["saldo"],
        "limite": conta["limite"]
    }
    arquivo.append(nova_conta)
    

def consultar(contas, nome):
    for conta in contas:
        if conta["nome"] == nome:
            return conta
    return None

def limite(conta, novo_limite):
    conta["limite"] = novo_limite

def deposito(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    if conta["saldo"] - valor >= -conta["limite"]:
        conta["saldo"] -= valor
        return True
    return False

def excluir(contas, nome):
    conta = consultar(contas, nome)
    if conta:
        contas.remove(conta)
        return True
    return False