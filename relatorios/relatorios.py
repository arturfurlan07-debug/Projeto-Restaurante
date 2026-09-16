def relatorio_vendas(pagamentos):
    """
    Recebe a Lista de pagamentos e mostra o total vendido e o total
    separado por forma de pagamento.
    """
    total_geral = 0
    total_por_forma = {}

    for pagamento in pagamentos.obter_todos():
        total_geral += pagamento.valor_total
        if pagamento.forma_pagamento not in total_por_forma:
            total_por_forma[pagamento.forma_pagamento] = 0
        total_por_forma[pagamento.forma_pagamento] += pagamento.valor_total

    print("===== RELATÓRIO DE VENDAS =====")
    print(f"Total geral vendido: R$ {total_geral:.2f}")
    for forma in total_por_forma:
        print(f"  {forma}: R$ {total_por_forma[forma]:.2f}")
    print("================================")


def relatorio_consumo(comandas_fechadas):
    """
    Recebe a lista de comandas já fechadas (vinda da Pilha de histórico)
    e mostra quanto foi consumido de cada produto no total.
    """
    consumo_por_produto = {}

    for comanda in comandas_fechadas:
        for item in comanda.itens.obter_todos():
            if item.nome not in consumo_por_produto:
                consumo_por_produto[item.nome] = 0
            consumo_por_produto[item.nome] += item.quantidade

    print("===== RELATÓRIO DE CONSUMO =====")
    for nome_produto in consumo_por_produto:
        print(f"  {nome_produto}: {consumo_por_produto[nome_produto]} unidades")
    print("=================================")
