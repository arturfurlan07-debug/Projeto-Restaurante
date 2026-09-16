from estruturas.no import No


class Pilha:
    """
    Pilha (LIFO - Last In, First Out) implementada com nós encadeados.
    Usada para guardar o histórico de comandas já fechadas/pagas,
    de forma que a última comanda fechada é a primeira a aparecer
    no histórico (útil para conferência rápida do caixa).
    """

    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def esta_vazia(self):
        return self._topo is None

    def empilhar(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self._topo
        self._topo = novo_no
        self._tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None
        no_removido = self._topo
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return no_removido.dado

    def topo(self):
        return None if self.esta_vazia() else self._topo.dado

    def para_lista_python(self):
        resultado = []
        atual = self._topo
        while atual is not None:
            resultado.append(atual.dado)
            atual = atual.proximo
        return resultado

    def __iter__(self):
        atual = self._topo
        while atual is not None:
            yield atual.dado
            atual = atual.proximo
