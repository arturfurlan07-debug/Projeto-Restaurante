class Produto:
    """
    Representa um produto do estoque (ingrediente, bebida etc.).
    Guarda também a data de vencimento, pois os produtos são perecíveis
    e o uso deve priorizar os mais antigos.
    """

    def __init__(self, nome, preco_compra, preco_venda, data_compra,
                 data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def editar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def __repr__(self):
        return (f"Produto(nome={self.nome!r}, qtd={self.quantidade}, "
                f"vencimento={self.data_vencimento})")
