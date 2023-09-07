class CaixaRegistradora:
    def __init__(self):
        self._total_venda = 0
        self._numero_itens = 0

    def add_item(self, preco, quantidade):
        self._total_venda += preco * quantidade
        self._numero_itens += quantidade

    def finalizar_venda(self):
        print("Obrigado por comprar conosco!")
        print(f"Foram comprados {self._numero_itens} itens")
        print(f"TOTAL: R${self._total_venda:.2f}")
        print("=" * 50)

        self._total_venda = 0
        self._numero_itens = 0

## Programa Principal
mercado = CaixaRegistradora()

mercado.add_item(1.5, 2)
mercado.add_item(15.2, 1)
mercado.add_item(39.4, 6)

# É possível acessar essas variáveis, mas por convenção não devemos fazer isso
#mercado._total_venda = -0.5
#mercado._numero_itens = -10

mercado.finalizar_venda()

print(dir(mercado))