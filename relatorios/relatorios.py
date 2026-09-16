def relatorio_vendas(pagamentos):
    """
    Recebe a lista de pagamentos e retorna um resumo:
    total vendido e total por forma de pagamento.
    """
    total_geral = 0.0
    por_forma = {}
    for pagamento in pagamentos:
        total_geral += pagamento.valor_total
        por_forma[pagamento.forma_pagamento] = (
            por_forma.get(pagamento.forma_pagamento, 0.0) + pagamento.valor_total
        )

    print("===== RELATÓRIO DE VENDAS =====")
    print(f"Total geral vendido: R$ {total_geral:.2f}")
    for forma, valor in por_forma.items():
        print(f"  - {forma}: R$ {valor:.2f}")
    print("================================")
    return {"total_geral": total_geral, "por_forma_pagamento": por_forma}


def relatorio_consumo(comandas_fechadas):
    """
    Recebe uma lista/iterável de comandas já fechadas e retorna
    a quantidade total consumida de cada produto.
    """
    consumo_por_produto = {}
    for comanda in comandas_fechadas:
        for item in comanda.itens:
            consumo_por_produto[item.nome_produto] = (
                consumo_por_produto.get(item.nome_produto, 0) + item.quantidade
            )

    print("===== RELATÓRIO DE CONSUMO =====")
    for nome_produto, quantidade in consumo_por_produto.items():
        print(f"  - {nome_produto}: {quantidade} unidades")
    print("=================================")
    return consumo_por_produto
