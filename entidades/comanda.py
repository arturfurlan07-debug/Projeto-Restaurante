from colecoes.lista import Lista


class Comanda:
    """
    Comanda de um cliente: número, nome, data/hora de abertura e os
    itens pedidos (refeições e bebidas), guardados em uma Lista própria.
    """

    def __init__(self, numero, nome_cliente, data_abertura):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.data_abertura = data_abertura
        self.itens = Lista()
        self.status = "aberta"
        self.data_fechamento = None

    def adicionar_item(self, item):
        if self.status == "fechada":
            raise ValueError("Não é possível adicionar itens a uma comanda fechada.")
        self.itens.inserir_fim(item)

    def remover_item(self, nome_item):
        if self.status == "fechada":
            raise ValueError("Não é possível remover itens de uma comanda fechada.")
        return self.itens.remover_por_nome(nome_item)

    def calcular_total(self):
        total = 0
        for item in self.itens.obter_todos():
            total += item.calcular_valor()
        return total

    def fechar(self, data_fechamento):
        self.status = "fechada"
        self.data_fechamento = data_fechamento

    def __str__(self):
        return f"Comanda nº{self.numero} - {self.nome_cliente} ({self.status})"
