from estruturas.no import No


class ListaEncadeada:
    """
    Lista encadeada simples, implementada do zero com nós (No).
    Usada, por exemplo, para armazenar as refeições e bebidas de uma comanda,
    e também como base para o estoque (mantendo os produtos ordenados por
    data de vencimento, do mais velho para o mais novo).
    """

    def __init__(self):
        self._cabeca = None
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def esta_vazia(self):
        return self._cabeca is None

    def adicionar(self, dado):
        """Adiciona um item ao final da lista."""
        novo_no = No(dado)
        if self._cabeca is None:
            self._cabeca = novo_no
        else:
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self._tamanho += 1

    def adicionar_ordenado(self, dado, chave):
        """
        Insere o item mantendo a lista ordenada de forma crescente,
        de acordo com a função `chave(dado)`.
        Usado no estoque para manter os produtos mais próximos do
        vencimento sempre no início da lista.
        """
        novo_no = No(dado)
        if self._cabeca is None or chave(dado) < chave(self._cabeca.dado):
            novo_no.proximo = self._cabeca
            self._cabeca = novo_no
        else:
            atual = self._cabeca
            while atual.proximo is not None and chave(atual.proximo.dado) <= chave(dado):
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
        self._tamanho += 1

    def remover(self, condicao):
        """
        Remove o primeiro item que satisfaz `condicao(dado)` e o retorna.
        Retorna None se nenhum item for encontrado.
        """
        anterior = None
        atual = self._cabeca
        while atual is not None:
            if condicao(atual.dado):
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return atual.dado
            anterior = atual
            atual = atual.proximo
        return None

    def buscar(self, condicao):
        """Retorna o primeiro item que satisfaz `condicao(dado)`, ou None."""
        atual = self._cabeca
        while atual is not None:
            if condicao(atual.dado):
                return atual.dado
            atual = atual.proximo
        return None

    def para_lista_python(self):
        """
        Converte para uma list nativa apenas para facilitar iteração/exibição
        fora da estrutura (ex.: relatórios). A estrutura de dados em si
        continua sendo a lista encadeada.
        """
        resultado = []
        atual = self._cabeca
        while atual is not None:
            resultado.append(atual.dado)
            atual = atual.proximo
        return resultado

    def __iter__(self):
        atual = self._cabeca
        while atual is not None:
            yield atual.dado
            atual = atual.proximo

    def __repr__(self):
        return f"ListaEncadeada({self.para_lista_python()!r})"
