class ItemPedido:
    """
    Representa um item (refeição ou bebida) pedido dentro de uma comanda.
    `tipo` é "refeicao" ou "bebida", usado para separar os relatórios
    de consumo e para saber de onde dar baixa no estoque.
    """

    def __init__(self, nome_produto, tipo, quantidade, preco_unitario):
        self.nome_produto = nome_produto
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def valor_total(self):
        return self.quantidade * self.preco_unitario

    def __repr__(self):
        return f"ItemPedido({self.tipo}: {self.nome_produto} x{self.quantidade})"
