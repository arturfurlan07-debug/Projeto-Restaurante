class No:
    """
    Um nó guarda um dado e a referência para o próximo nó.
    É a peça básica usada para montar a Lista, a Fila e a Pilha,
    sem usar list, deque ou qualquer estrutura pronta do Python.
    """

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
