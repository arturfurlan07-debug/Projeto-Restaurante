from estruturas.lista_encadeada import ListaEncadeada


class Estoque:
    """
    Gerencia os produtos do restaurante usando uma Lista Encadeada
    própria, mantida ordenada por data de vencimento. Dessa forma,
    ao dar baixa em um produto, o item mais próximo do vencimento
    (mais velho) é sempre o primeiro a ser consumido.
    """

    def __init__(self):
        self._produtos = ListaEncadeada()

    def adicionar_produto(self, produto):
        # insere já na posição correta, ordenado pela data de vencimento
        self._produtos.adicionar_ordenado(produto, chave=lambda p: p.data_vencimento)

    def buscar_por_nome(self, nome):
        """
        Retorna o produto com esse nome que estiver mais próximo do
        vencimento (o primeiro encontrado, pois a lista já está ordenada).
        """
        return self._produtos.buscar(lambda p: p.nome == nome and p.quantidade > 0)

    def editar_quantidade(self, nome, nova_quantidade):
        produto = self._produtos.buscar(lambda p: p.nome == nome)
        if produto is None:
            raise ValueError(f"Produto '{nome}' não encontrado no estoque.")
        produto.editar_quantidade(nova_quantidade)

    def dar_baixa(self, nome, quantidade_consumida):
        """
        Reduz a quantidade em estoque do produto indicado, sempre a
        partir do lote mais antigo (mais próximo do vencimento).
        Lança erro se não houver estoque suficiente.
        """
        produto = self.buscar_por_nome(nome)
        if produto is None or produto.quantidade < quantidade_consumida:
            raise ValueError(f"Estoque insuficiente para o produto '{nome}'.")
        produto.quantidade -= quantidade_consumida

    def listar_produtos(self):
        return self._produtos.para_lista_python()

    def __repr__(self):
        return f"Estoque({len(self._produtos)} produtos)"
