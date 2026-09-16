from colecoes.lista import Lista


class Estoque:
    """
    Guarda os produtos do restaurante em uma Lista própria.

    Ao dar baixa em um produto, sempre procura primeiro o produto
    mais próximo do vencimento (o mais velho) entre os que têm esse
    nome e ainda têm quantidade disponível — como pede o enunciado.
    """

    def __init__(self):
        self.produtos = Lista()

    def adicionar_produto(self, produto):
        self.produtos.inserir_fim(produto)

    def editar_quantidade(self, nome, nova_quantidade):
        produto = self.produtos.buscar_por_nome(nome)
        if produto is None:
            raise ValueError(f"Produto '{nome}' não encontrado no estoque.")
        produto.editar_quantidade(nova_quantidade)

    def buscar_produto_mais_antigo(self, nome):
        """
        Percorre todos os produtos com esse nome e retorna, entre os
        que têm quantidade disponível, o que está mais perto de vencer.
        """
        produto_mais_antigo = None
        for produto in self.produtos.obter_todos():
            if produto.nome == nome and produto.quantidade > 0:
                if produto_mais_antigo is None or produto.data_vencimento < produto_mais_antigo.data_vencimento:
                    produto_mais_antigo = produto
        return produto_mais_antigo

    def dar_baixa(self, nome, quantidade_usada):
        produto = self.buscar_produto_mais_antigo(nome)
        if produto is None or produto.quantidade < quantidade_usada:
            raise ValueError(f"Estoque insuficiente para '{nome}'.")
        produto.quantidade -= quantidade_usada
