from colecoes.no import No


class Pilha:
    """
    Pilha (LIFO): o último que entra é o primeiro que sai.
    Usada para o histórico de comandas já fechadas: a última
    comanda paga fica sempre no topo, fácil de consultar.
    """

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None
        no_removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return no_removido.dado

    def obter_todos(self):
        todos = []
        atual = self.topo
        while atual is not None:
            todos.append(atual.dado)
            atual = atual.proximo
        return todos
