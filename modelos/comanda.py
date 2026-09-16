from estruturas.lista_encadeada import ListaEncadeada


class Comanda:
    """
    Representa a comanda de um cliente: número, nome, data/hora de
    abertura, e os itens (refeições e bebidas) pedidos ao longo do
    atendimento. Os itens ficam em uma Lista Encadeada própria.
    """

    def __init__(self, numero, nome_cliente, data_hora_abertura):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.data_hora_abertura = data_hora_abertura
        self.itens = ListaEncadeada()
        self.aberta = True
        self.data_hora_fechamento = None

    def adicionar_item(self, item_pedido):
        """Adiciona uma refeição ou bebida à comanda (antes do fechamento)."""
        if not self.aberta:
            raise ValueError("Não é possível adicionar itens a uma comanda fechada.")
        self.itens.adicionar(item_pedido)

    def remover_item(self, nome_produto):
        """Remove um item da comanda pelo nome do produto."""
        if not self.aberta:
            raise ValueError("Não é possível remover itens de uma comanda fechada.")
        return self.itens.remover(lambda item: item.nome_produto == nome_produto)

    def valor_total(self):
        return sum(item.valor_total() for item in self.itens)

    def fechar(self, data_hora_fechamento):
        self.aberta = False
        self.data_hora_fechamento = data_hora_fechamento

    def __repr__(self):
        status = "aberta" if self.aberta else "fechada"
        return f"Comanda(nº{self.numero}, {self.nome_cliente}, {status})"
