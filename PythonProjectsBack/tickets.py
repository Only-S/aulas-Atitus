class maquina:
    def __init__(self, preco):
        self.preco = preco
        self.valor = 0
        self.arrecadado = 0


    def inserir_dinheiro(self, vlr):
        self.valor += vlr


    def imprimir_ticket(self):
        if self.valor < self.preco:
            print(f"O dinheiro inserido na máquina ({self.valor} centavos) é insuficiente. Preço do Ticket: {self.preco} centavos")
        elif self.valor == self.preco:
            print(f"####################\n {'TICKET':^19} \n {f'{self.preco} centavos':^18}  \n####################")
            self.arrecadado += self.preco
            self.valor = 0
        else:
            print(f"####################\n {'TICKET':^19} \n {f'{self.preco} centavos':^18}  \nTroco: {self.valor - self.preco} centavos\n####################")
            self.arrecadado += self.preco
            self.valor = 0


maquina = maquina(int(input("Informe o preço do ticket: ")))#, True)
rodando = True

while rodando:
    opcao = input(f"MÁQUINA DE TICKETS: [possuo {maquina.valor} centavos]\n[a] Inserir Moedas\n[b] Imprimir Ticket\n[x] Encerrar Operação\n\t\t?")

    match opcao:
        case "a":
            vlr = 0
            while vlr != -1:
                vlr = int(input("Informe a moeda [-1 para parar]: "))
                if vlr < -1:
                    print("São aceitos apenas valores positivos ou \"-1\" para encerrar a inserção de moedas.")
                elif vlr == -1 or vlr == 0:
                    pass
                else:
                    maquina.inserir_dinheiro(vlr)
        case "b":
            maquina.imprimir_ticket()
        case "x":
            print(f"\nTotal Arrecadado: {maquina.arrecadado}")
            break

