from estruturas.no import No


class Fila:
    """
    Fila (FIFO - First In, First Out) implementada com nós encadeados.
    Usada para controlar as comandas abertas na ordem em que os
    clientes chegaram ao restaurante.
    """

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def esta_vazia(self):
        return self._inicio is None

    def enfileirar(self, dado):
        """Adiciona um item ao final da fila."""
        novo_no = No(dado)
        if self.esta_vazia():
            self._inicio = novo_no
            self._fim = novo_no
        else:
            self._fim.proximo = novo_no
            self._fim = novo_no
        self._tamanho += 1

    def desenfileirar(self):
        """Remove e retorna o item que está na frente da fila."""
        if self.esta_vazia():
            return None
        no_removido = self._inicio
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return no_removido.dado

    def remover_por_condicao(self, condicao):
        """
        Remove o primeiro item que satisfaz `condicao(dado)`, mesmo que
        não esteja no início da fila (necessário para fechar uma comanda
        específica, não necessariamente a mais antiga).
        """
        anterior = None
        atual = self._inicio
        while atual is not None:
            if condicao(atual.dado):
                if anterior is None:
                    self._inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual is self._fim:
                    self._fim = anterior
                self._tamanho -= 1
                return atual.dado
            anterior = atual
            atual = atual.proximo
        return None

    def buscar(self, condicao):
        atual = self._inicio
        while atual is not None:
            if condicao(atual.dado):
                return atual.dado
            atual = atual.proximo
        return None

    def para_lista_python(self):
        resultado = []
        atual = self._inicio
        while atual is not None:
            resultado.append(atual.dado)
            atual = atual.proximo
        return resultado

    def __iter__(self):
        atual = self._inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo
