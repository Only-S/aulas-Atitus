class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.marcha = 0
        self.esta_ligado = False

    def acelerar(self, vel):
        if self.esta_ligado:
            self.velocidade += vel
            print(f"Acelerando. Velocidade atual: {self.velocidade} km/h")
        else:
            print("O carro está desligado. Ligue-o para acelerar.")

    def frear(self):
        while self.velocidade > 0:
            self.velocidade -= 1
            print(f"{self.velocidade} km/h")

    def ligar(self):
        self.esta_ligado = True

    def desligar(self):
        self.esta_ligado = False

    def mudar_marcha(self):
        opcao = 0
        while opcao != 1 and opcao != 2:
            opcao = int(input("Você deseja:\n 1 - aumentar marcha\n 2 - reduzir marcha\nDigite o código da opção desejada:"))
            match opcao:
                case 1:
                    if self.marcha < 5:
                            self.marcha += 1
                            (f"Subiu 1 marcha. Marcha Atual: {self.marcha}ª marcha.")
                    else:
                        print(f"Você já está na marcha máxima! (Marcha atual {self.marcha}ª)")
                case 2:
                    if self.marcha > 0:
                        self.marcha -= 1
                        (f"Reduziu 1 marcha. Marcha Atual: {self.marcha}ª marcha.")
                    else:
                        print(f"Você já está na marcha mínima! (Marcha atual {self.marcha} - ponto morto)")
                case _:
                    print("Opção Inválida!\n")


carro1 = Carro("Fusca",1978,"Amarelo")
carro2 = Carro("Ferrari",2013,"Vermelho")
carro3 = Carro("Gol",2021,"Prata")

print(f"Cor do carro 1: {carro1.cor}")
print(f"Velocidade do carro 3: {carro3.velocidade}")
carro3.acelerar(50)
print(f"Cor do Carro 1: {carro1.cor}")
carro1.ligar()
carro1.acelerar(20)
carro1.mudar_marcha()
carro1.acelerar(30)
carro1.frear()
print(f"Velocidade do carro 1: {carro1.velocidade}")
print(f"Marcha do carro 1: {carro1.marcha}")
print(f"Velocidade do carro 1: {carro1.velocidade}")