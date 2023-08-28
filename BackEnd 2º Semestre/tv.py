'''TV DIGITAL:
ATRIBUTOS: Está Ligada?, Marca, Volume, Brilho
Métodos: Liga, Desliga, Aumenta Volume, Baixa Volume, Aumenta Brilho, Diminui Brilho
Classe: estaLigado: False, marca: LG, volume: 60, brilho: 50

TV ANALÓGICA:
ATRIBUTOS: Está Ligada?, Marca, Volume, Brilho
Métodos: Liga, Desliga, Aumenta Volume, Baixa Volume, Aumenta Brilho, Diminui Brilho
Classe: estaLigado: True, marca: Sony, volume: 20, brilho: 100'''

class Tv:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
        self.volume = 50
        self.brilho = 50
        self.esta_ligado = False

    def ligar(self):
        self.esta_ligado = True

    def desligar(self):
        self.esta_ligado = False

    def aumenta_volume(self, vol):
        while self.volume < vol:
            self.volume += 1
            print(f"-"*self.volume, f"{self.volume}%", end="")
        print()

    def reduz_volume(self, vol):
        while self.volume > vol:
            self.volume -= 1
            print(f"-"*self.volume, f"{self.volume}%", end="")
        print()

    def aumenta_brilho(self):
        pass

    def reduz_brilho(self):
        pass

tv1 = Tv("Samsung", "Digital")
tv2 = Tv("TeleFunken","Analógica")

print(f"{tv1.marca}")
tv1.aumenta_volume(100)
tv1.reduz_volume(60)

