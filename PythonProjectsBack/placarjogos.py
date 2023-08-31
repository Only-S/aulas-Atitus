class ItemPlacar:
    def __init__(self, nome, placar_obtido):
        self._nome = nome
        self._placar_obtido = placar_obtido

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self):
        _nome

    def __str__(self):
        return f"{self.nome}, {self.placar_obtido}"

class Placar:
    def __init__(self, tam_max = 5):
        self._tam_max = tam_max
        self._scores = []
        print(self._scores)

    def __str__(self):
        retorno = ""
        posicao = 1
        for placar in self._scores:
            retorno += str(posicao) + "-" + str(placar) + "\n"
            posicao += 1
        return retorno

    def inserir_item(self, item: ItemPlacar):
        self._scores.append(item)
        self._scores.sort(reverse=True)
        if len(self._scores) > self._tam_max:
            self._scores = self._scores[:self._tam_max]

    def __lt__(self, outroItem:
        return self._placar < outroItem._placar

    def __lt__(self, outroItem:
        return self._placar < outroItem._placar

    def __lt__(self, outroItem:
        return self._placar < outroItem._placar

    def __lt__(self, outroItem:
        return self._placar < outroItem._placar



'''item1 = ItemPlacar("JDG", 123)
item2 = ItemPlacar("VFG", 321)
item3 = ItemPlacar("POI", 231)
item4 = ItemPlacar("MNG", 132)
print(item1, item2, item3, item4)'''

p1 = ItemPlacar("JDG", 123)
p2 = ItemPlacar("VFG", 321)

print(p1 == p2)
print(p1 > p2)
print(p1 <= p2)