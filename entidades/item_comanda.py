class ItemComanda:
    """
    Uma refeição ou bebida pedida dentro de uma comanda.
    `tipo` é sempre "refeicao" ou "bebida".
    """

    def __init__(self, nome, tipo, quantidade, preco_unitario):
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_valor(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.nome} ({self.tipo})"
