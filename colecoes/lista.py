from colecoes.no import No


class Lista:
    """
    Lista encadeada simples, feita com nós (No).

    Guarda objetos que tenham um atributo `nome` (Produto e ItemComanda
    têm esse atributo), permitindo buscar e remover pelo nome.
    Usada para os itens de uma comanda e para os produtos do estoque.
    """

    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.primeiro is None

    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def buscar_por_nome(self, nome):
        atual = self.primeiro
        while atual is not None:
            if atual.dado.nome == nome:
                return atual.dado
            atual = atual.proximo
        return None

    def remover_por_nome(self, nome):
        anterior = None
        atual = self.primeiro
        while atual is not None:
            if atual.dado.nome == nome:
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual.dado
            anterior = atual
            atual = atual.proximo
        return None

    def obter_todos(self):
        """
        Percorre a lista encadeada e devolve os dados em uma list comum,
        só para facilitar a exibição em relatórios. A estrutura que
        guarda os dados de verdade continua sendo os nós encadeados acima.
        """
        todos = []
        atual = self.primeiro
        while atual is not None:
            todos.append(atual.dado)
            atual = atual.proximo
        return todos
