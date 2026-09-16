class Pagamento:
    """
    Representa o pagamento realizado no fechamento de uma comanda.
    """

    FORMAS_VALIDAS = ("PIX", "Cartão", "Dinheiro")

    def __init__(self, nome_pagador, numero_comanda, forma_pagamento,
                 valor_total, data_hora):
        if forma_pagamento not in self.FORMAS_VALIDAS:
            raise ValueError(f"Forma de pagamento inválida: {forma_pagamento}")
        self.nome_pagador = nome_pagador
        self.numero_comanda = numero_comanda
        self.forma_pagamento = forma_pagamento
        self.valor_total = valor_total
        self.data_hora = data_hora

    def __repr__(self):
        return (f"Pagamento(comanda nº{self.numero_comanda}, "
                f"{self.forma_pagamento}, R${self.valor_total:.2f})")
