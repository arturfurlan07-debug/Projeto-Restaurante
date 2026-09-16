class No:
    """
    Nó genérico usado pelas estruturas encadeadas (Lista, Fila, Pilha).
    Guarda um dado e a referência para o próximo nó.
    """

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __repr__(self):
        return f"No({self.dado!r})"
