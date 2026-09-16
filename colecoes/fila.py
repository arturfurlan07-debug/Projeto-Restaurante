from colecoes.no import No


class Fila:
    """
    Fila (FIFO): o primeiro que entra é o primeiro que sai.
    Usada para guardar as comandas abertas, na ordem em que os
    clientes chegaram no restaurante.
    """

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def buscar_por_numero(self, numero):
        atual = self.inicio
        while atual is not None:
            if atual.dado.numero == numero:
                return atual.dado
            atual = atual.proximo
        return None

    def remover_por_numero(self, numero):
        anterior = None
        atual = self.inicio
        while atual is not None:
            if atual.dado.numero == numero:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual == self.fim:
                    self.fim = anterior
                self.tamanho -= 1
                return atual.dado
            anterior = atual
            atual = atual.proximo
        return None

    def obter_todos(self):
        todos = []
        atual = self.inicio
        while atual is not None:
            todos.append(atual.dado)
            atual = atual.proximo
        return todos
