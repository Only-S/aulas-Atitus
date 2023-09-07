class CaixaRegistradora:
    def __init__(self):
        self._total_venda = 0
        self._numero_itens = 0

    def get_total_venda(self):
        return self._total_venda

    def set_total_venda(self, valor):
        self._total_venda = valor

    def get_numero_itens(self):
        return self._numero_itens

    def set_numero_itens(self, valor):
        self._numero_itens = valor

    def add_item(self, preco, quantidade):
        self._total_venda += preco * quantidade
        self._numero_itens += quantidade

    def finalizar_venda(self):
        print("Obrigado por comprar conosco!")
        print(f"Foram comprados {self.get_numero_itens()} itens")
        print(f"TOTAL: R${self.get_total_venda():.2f}")
        print("=" * 50)

        self.set_total_venda(0)
        self.set_numero_itens(0)

## Programa Principal
mercado = CaixaRegistradora()

mercado.add_item(1.5, 2)
mercado.add_item(15.2, 1)
mercado.add_item(39.4, 6)

mercado.finalizar_venda()
