class Carro:
    def __init__(self, marca, ano, cor):
        self.cor = cor
        self.ano = ano
        self.marca = marca
        self.velocidade = 0
        self.marcha = 0
        self.esta_ligado = False
        #classe nao devolve nada, nao pode usar return

    def __str__(self):
        return f"{self.marca} - {self.ano}"

    def ligar(self):
        self.esta_ligado = True

    def desligar(self):
        self.esta_ligado = False
        self.velocidade = 0
        self.marcha = 0

    def acelerar(self, velocidade):
        if self.esta_ligado:
            self.velocidade =

    def Frear(0):
        if self.esta_ligado:
            if self.velocidade > velocidade:
                self.velocidade = 0
            else:
                self.velocidade -= velocidade
        self.velocidade =

    def MudarMarcha(self):



#programa principal
if __name__ == "__main__"
    meu_carro = Carro("Ferrari", 2022, "Vermelho")
    meu_carro.abacaxi = "Qualquer coisa"
    print(meu_carro.abacaxi)
