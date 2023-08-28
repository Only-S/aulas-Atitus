import gerenciamento
import manipulacao

arquivo = manipulacao.carregar()

print("Olá! Seja bem vindo ao banco NemEx!\n\nSelecione abaixo qual serviço deseja utilizar!\n")

while True:
    print(" 1 - Criar Conta\n 2 - Consultar Conta\n 3 - Atualizar Limite\n 4 - Realizar depósito\n 5 - Realizar saque\n 6 - Excluir Conta\n 7 - Sair\n")

    try:
        escolha = int(input("Digite o código referente à operação escolhida: "))

        match escolha:
            case 1:
                conta = {
                    "nome": input("\nNome do correntista: ").lower(),
                    "email": input("E-mail do correntista: ").lower(),
                    "saldo": 0.0,
                    "limite": 1000.0
                }            
                gerenciamento.criar(arquivo, conta)
                manipulacao.grava(arquivo)
                print("\nConta Corrente criada com sucesso!\n")
            case 2:
                nome = input("\nNome do correntista: ").lower()
                conta = gerenciamento.consultar(arquivo, nome)
                if conta:
                    print(f"\nNome: {conta['nome']}\nE-mail: {conta['email']}\nSaldo: {conta['saldo']:.2f}\nLimite: {conta['limite']:.2f}\n")
                else:
                    print("\nCorrentista inexistente!\n")            
            case 3:
                nome = input("\nNome do correntista: ").lower()
                conta = gerenciamento.consultar(arquivo, nome)
                if conta:
                    novo_limite = float(input("Novo limite: "))
                    gerenciamento.limite(conta, novo_limite)
                    manipulacao.grava(arquivo)
                    print("\nLimite atualizado com sucesso!\n")
                else:
                    print("\nCorrentista inexistente!\n")
            case 4:
                nome = input("\nNome do correntista: ").lower()
                conta = gerenciamento.consultar(arquivo, nome)
                if conta:
                    valor = float(input("Valor do depósito: "))
                    gerenciamento.deposito(conta, valor)
                    manipulacao.grava(arquivo)
                    print("\nDepósito realizado com sucesso!\n")
                else:
                    print("\nCorrentista inexistente!\n")
            case 5:
                nome = input("\nNome do correntista: ").lower()
                conta = gerenciamento.consultar(arquivo, nome)
                if conta:
                    valor = float(input("Valor do saque: "))
                    if gerenciamento.saque(conta, valor):
                        manipulacao.grava(arquivo)
                        print("\nSaque realizado com sucesso!\n")
                    else:
                        print("\nSaldo insuficiente ou limite atingido.\n")
                else:
                    print("\nCorrentista inexistente!\n")
            case 6:
                nome = input("\nNome do correntista: ").lower()
                if gerenciamento.excluir(arquivo, nome):
                    manipulacao.grava(arquivo)
                    print("\nConta removida com sucesso!\n")
                else:
                    print("\nCorrentista inexistente!\n")
            case 7:
                print("\nEncerrando seu acesso, obrigado por estar conosco!\n...")
                break
            case _:
                print("\nOpção inválida! Você deve selecionar o dígito de uma das opções listadas.\n")
    except ValueError:
        print("\nOpção inválida! Você deve selecionar o dígito de uma das opções listadas.\n")