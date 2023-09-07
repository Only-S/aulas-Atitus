class Tv:
    def __init__(self, nome_rede = ''):
        self.canal = 12
        self.volume = 0
        self.brilho = 0
        self.contraste = 0
        self.estaLigada = False
        self.nomeRede = nome_rede

    def ligar(self):
        self.estaLigada = True

    def desligar(self):
        self.estaLigada = False

    def aumenta_volume(self):
        if self.estaLigada:
            self.volume += 1
        else:
            print("A TV está desligada")

    def diminui_volume(self):
        if self.estaLigada:
            self.volume -= 1
        else:
            print("A TV está desligada")

    def troca_canal(self):
        if self.estaLigada:
            self.canal += 1
        else:
            print("A TV está desligada")

    def aumenta_brilho(self):
        if self.estaLigada:
            self.brilho += 1
        else:
            print("A TV está desligada")

    def dimniui_brilho(self):
        if self.estaLigada:
            self.brilho -= 1
        else:
            print("A TV está desligada")

    def mudar_rede(self):
        if self.estaLigada:
            self.nomeRede = input("Insira o nome da rede: ")
        else:
            print("A TV está desligada")


tv_moderna = Tv("zézinP2P")
tv_antiga = Tv()
print(f"{tv_moderna.canal}")
