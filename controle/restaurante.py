from datetime import datetime

from colecoes.fila import Fila
from colecoes.pilha import Pilha
from colecoes.lista import Lista
from entidades.comanda import Comanda
from entidades.item_comanda import ItemComanda
from entidades.pagamento import Pagamento


class Restaurante:
    """
    Classe principal que junta tudo: abertura de comandas, inclusão e
    remoção de itens, fechamento (com baixa de estoque e pagamento) e
    histórico das comandas já atendidas.

    - `comandas_abertas`: Fila própria, na ordem de chegada dos clientes.
    - `historico_comandas`: Pilha própria, última comanda fechada no topo.
    - `pagamentos`: Lista própria, com todos os pagamentos registrados.
    """

    def __init__(self, estoque):
        self.estoque = estoque
        self.comandas_abertas = Fila()
        self.historico_comandas = Pilha()
        self.pagamentos = Lista()
        self.proximo_numero = 1

    def abrir_comanda(self, nome_cliente, data_abertura=None):
        if data_abertura is None:
            data_abertura = datetime.now()
        comanda = Comanda(self.proximo_numero, nome_cliente, data_abertura)
        self.proximo_numero += 1
        self.comandas_abertas.enfileirar(comanda)
        return comanda

    def adicionar_item(self, numero_comanda, nome_item, tipo, quantidade):
        comanda = self.comandas_abertas.buscar_por_numero(numero_comanda)
        if comanda is None:
            raise ValueError(f"Comanda nº{numero_comanda} não está aberta.")

        produto = self.estoque.buscar_produto_mais_antigo(nome_item)
        if produto is None:
            raise ValueError(f"Produto '{nome_item}' não encontrado no estoque.")

        item = ItemComanda(nome_item, tipo, quantidade, produto.preco_venda)
        comanda.adicionar_item(item)
        return item

    def remover_item(self, numero_comanda, nome_item):
        comanda = self.comandas_abertas.buscar_por_numero(numero_comanda)
        if comanda is None:
            raise ValueError(f"Comanda nº{numero_comanda} não está aberta.")
        return comanda.remover_item(nome_item)

    def fechar_comanda(self, numero_comanda, forma_pagamento, data_hora=None):
        if data_hora is None:
            data_hora = datetime.now()

        comanda = self.comandas_abertas.remover_por_numero(numero_comanda)
        if comanda is None:
            raise ValueError(f"Comanda nº{numero_comanda} não está aberta.")

        # baixa no estoque de cada item consumido na comanda
        for item in comanda.itens.obter_todos():
            self.estoque.dar_baixa(item.nome, item.quantidade)

        comanda.fechar(data_hora)
        valor_total = comanda.calcular_total()

        pagamento = Pagamento(
            comanda.nome_cliente,
            comanda.numero,
            forma_pagamento,
            valor_total,
            data_hora,
        )
        self.pagamentos.inserir_fim(pagamento)
        self.historico_comandas.empilhar(comanda)
        return pagamento
