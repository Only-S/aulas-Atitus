class ItemPlacar:
    def __init__(self, nome, placar):
        self._nome = nome
        self._placar = placar

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def placar(self):
        return self._placar

    @placar.setter
    def placar(self, valor):
        self._placar = valor

    def __str__(self):
        return f"{self._nome:10}\t{self._placar:5}"

    def __lt__(self, outroItem):
        return self._placar < outroItem._placar

    def __gt__(self, outroItem):
        return self._placar > outroItem._placar

    def __eq__(self, outroItem):
        return self._placar == outroItem._placar

    def __le__(self, outroItem):
        return self._placar <= outroItem._placar

    def __ge__(self, outroItem):
        return self._placar >= outroItem._placar

    def __ne__(self, outroItem):
        return self._placar != outroItem._placar

class Placar:
    def __init__(self, tam_max=5):
        self._tam_max = tam_max
        self._scores = []

    def inserir_item(self, item: ItemPlacar):
        self._scores.append(item)
        self._scores.sort(reverse=True)
        if len(self._scores) > self._tam_max:
            self._scores = self._scores[:self._tam_max]
    def __str__(self):
        placar = '\n'
        for item in self._scores:
            placar += f"{item}\n"
        return placar

'''p1 = ItemPlacar("AAA", 123)
p2 = ItemPlacar("ZZZ", 123)

print(p1 == p2)
print(p1 > p2)
print(p1 <= p2)'''

placar = Placar(4)
placar.inserir_item(ItemPlacar("AAA", 123))
placar.inserir_item(ItemPlacar("BBB", 234))
placar.inserir_item(ItemPlacar("CCC", 200))
placar.inserir_item(ItemPlacar("DDD", 100))
placar.inserir_item(ItemPlacar("EEE", 400))
placar.inserir_item(ItemPlacar("FFF", 99))
placar.inserir_item(ItemPlacar("GGG", 150))
print(placar)