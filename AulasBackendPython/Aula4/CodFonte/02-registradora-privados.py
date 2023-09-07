class CaixaRegistradora:
    def __init__(self):
        self.__total_venda = 0
        self.__numero_itens = 0

    def add_item(self, preco, quantidade):
        self.__total_venda += preco * quantidade
        self.__numero_itens += quantidade

    def finalizar_venda(self):
        print("Obrigado por comprar conosco!")
        print(f"Foram comprados {self.__numero_itens} itens")
        print(f"TOTAL: R${self.__total_venda:.2f}")
        print("=" * 50)

        self.__total_venda = 0
        self.__numero_itens = 0

## Programa Principal
mercado = CaixaRegistradora()

mercado.add_item(1.5, 2)
mercado.add_item(15.2, 1)
mercado.add_item(39.4, 6)

mercado.total_venda = -0.5
mercado.numero_itens = -10

mercado.finalizar_venda()