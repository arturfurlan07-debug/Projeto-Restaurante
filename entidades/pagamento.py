class Pagamento:
    """
    Registro do pagamento feito no fechamento de uma comanda.
    """

    FORMAS_ACEITAS = ["PIX", "Cartão", "Dinheiro"]

    def __init__(self, nome_pagador, numero_comanda, forma_pagamento, valor_total, data_hora):
        if forma_pagamento not in self.FORMAS_ACEITAS:
            raise ValueError(f"Forma de pagamento inválida: {forma_pagamento}")
        self.nome_pagador = nome_pagador
        self.numero_comanda = numero_comanda
        self.forma_pagamento = forma_pagamento
        self.valor_total = valor_total
        self.data_hora = data_hora

    def __str__(self):
        return f"Pagamento da comanda nº{self.numero_comanda}: R$ {self.valor_total:.2f} via {self.forma_pagamento}"
