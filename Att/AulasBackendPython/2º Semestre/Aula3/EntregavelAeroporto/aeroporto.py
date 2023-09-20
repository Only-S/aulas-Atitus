class Piloto:
    def __init__(self, nome, breve, horas_voo):
        self.nome = nome
        self.breve = breve
        self.horasVoo = horas_voo

    def realizar_voo(self, tempo_voo):
        self.horasVoo += tempo_voo

    def __str__(self):
        return f"\nPiloto: {self.nome}\nBrevê: {self.breve}\nPossui {self.horasVoo} horas de voo\n"


class Aviao:
    def __init__(self, marca, modelo, capacidade, min_horas):
        self.marca = marca
        self.modelo = modelo
        self.capacidade = capacidade
        self.piloto = None
        self.horas_minimas = min_horas

    def inserir_piloto(self, piloto):
        if piloto.horasVoo >= self.horas_minimas:
            self.piloto = piloto
            print(f"O piloto {piloto.nome} é o novo piloto do {self.marca} - {self.modelo}")
            return True
        else:
            print(f"O Piloto não está autorizado a operar este avião!")
            return False

    def voar(self, tempo):
        if self.piloto:
            print(f"{self.marca} - {self.modelo} decolando com o piloto {self.piloto}")
            self.piloto.realizar_voo(tempo)
        else:
            print("Impossível voar! Não tenho piloto!\n")

    def __str__(self):
        resultado = f"\nAvião {self.marca} - {self.modelo} com capacidade para {self.capacidade} passageiros "
        if self.piloto:
            return resultado + f"Pilotado por:\n{self.piloto.nome}"
        else:
            return resultado + f"Não possuí piloto\n"


piloto1 = Piloto("José da Silva", 123456, 2000)
piloto2 = Piloto("Maria das Graças", 456789, 19350)

aviao1 = Aviao("Boeing", "737", 215, 1000)
aviao2 = Aviao("AirBus", "A320", 200, 3000)
aviao3 = Aviao("Northrop", "f5", 1, 30000)

print(piloto1, piloto2)
print(aviao1, aviao2, aviao3)

aviao1.inserir_piloto(piloto1)
aviao2.inserir_piloto(piloto1)
aviao3.inserir_piloto(piloto1)
aviao2.inserir_piloto(piloto2)
aviao3.inserir_piloto(piloto2)

print(aviao1, aviao2, aviao3)

aviao1.voar(20)
aviao2.voar(20)
aviao3.voar(20)

print(piloto1, piloto2)

piloto1.realizar_voo(27980)
aviao3.inserir_piloto(piloto1)
aviao3.voar(5)