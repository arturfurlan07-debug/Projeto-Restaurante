from datetime import datetime

from estruturas.fila import Fila
from estruturas.pilha import Pilha
from modelos.comanda import Comanda
from modelos.item_pedido import ItemPedido
from modelos.pagamento import Pagamento


class Restaurante:
    """
    Classe central que simula o funcionamento do restaurante:
    abertura de comandas, inclusão/remoção de itens, fechamento
    (com baixa de estoque e pagamento) e histórico.

    - `comandas_abertas`: Fila própria (ordem de chegada dos clientes).
    - `historico_comandas`: Pilha própria (última comanda fechada primeiro).
    """

    def __init__(self, estoque):
        self.estoque = estoque
        self.comandas_abertas = Fila()
        self.historico_comandas = Pilha()
        self.pagamentos = []  # lista simples só para relatórios finais
        self._proximo_numero = 1

    def abrir_comanda(self, nome_cliente, data_hora=None):
        data_hora = data_hora or datetime.now()
        comanda = Comanda(self._proximo_numero, nome_cliente, data_hora)
        self._proximo_numero += 1
        self.comandas_abertas.enfileirar(comanda)
        return comanda

    def _buscar_comanda_aberta(self, numero_comanda):
        comanda = self.comandas_abertas.buscar(lambda c: c.numero == numero_comanda)
        if comanda is None:
            raise ValueError(f"Comanda nº{numero_comanda} não está aberta.")
        return comanda

    def adicionar_item(self, numero_comanda, nome_produto, tipo, quantidade):
        """tipo: 'refeicao' ou 'bebida'."""
        comanda = self._buscar_comanda_aberta(numero_comanda)
        produto = self.estoque.buscar_por_nome(nome_produto)
        if produto is None:
            raise ValueError(f"Produto '{nome_produto}' não encontrado no estoque.")
        item = ItemPedido(nome_produto, tipo, quantidade, produto.preco_venda)
        comanda.adicionar_item(item)
        return item

    def remover_item(self, numero_comanda, nome_produto):
        comanda = self._buscar_comanda_aberta(numero_comanda)
        return comanda.remover_item(nome_produto)

    def fechar_comanda(self, numero_comanda, forma_pagamento, data_hora=None):
        """
        Fecha a comanda: dá baixa no estoque de tudo que foi consumido,
        registra o pagamento e move a comanda para o histórico (pilha).
        """
        data_hora = data_hora or datetime.now()
        comanda = self.comandas_abertas.remover_por_condicao(
            lambda c: c.numero == numero_comanda
        )
        if comanda is None:
            raise ValueError(f"Comanda nº{numero_comanda} não está aberta.")

        # baixa no estoque de cada item consumido
        for item in comanda.itens:
            self.estoque.dar_baixa(item.nome_produto, item.quantidade)

        comanda.fechar(data_hora)
        valor_total = comanda.valor_total()

        pagamento = Pagamento(
            nome_pagador=comanda.nome_cliente,
            numero_comanda=comanda.numero,
            forma_pagamento=forma_pagamento,
            valor_total=valor_total,
            data_hora=data_hora,
        )
        self.pagamentos.append(pagamento)
        self.historico_comandas.empilhar(comanda)
        return pagamento
