class Produto:
    """
    Um produto do estoque (ingrediente ou bebida).
    Guarda a data de vencimento porque os produtos são perecíveis.
    """

    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def editar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def __str__(self):
        data_formatada = self.data_vencimento.strftime("%d/%m/%Y")
        return f"{self.nome} (qtd: {self.quantidade}, vence em {data_formatada})"
