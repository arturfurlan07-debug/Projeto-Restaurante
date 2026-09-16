from servicos.estoque import Estoque
from servicos.restaurante import Restaurante
from gerador.gerador_dados import gerar_produtos_estoque, gerar_nome_cliente
from persistencia.persistencia import salvar_dados, carregar_dados
from relatorios.relatorios import relatorio_vendas, relatorio_consumo

CAMINHO_DADOS = "dados/restaurante.pkl"


def montar_estoque_inicial():
    estoque = Estoque()
    for produto in gerar_produtos_estoque():
        estoque.adicionar_produto(produto)
    return estoque


def simular_atendimento(restaurante):
    # abertura da comanda
    comanda = restaurante.abrir_comanda(gerar_nome_cliente())
    print(f"Comanda aberta: {comanda}")

    # inclusão de refeição(ões) e bebida(s)
    restaurante.adicionar_item(comanda.numero, "Feijoada", "refeicao", 1)
    restaurante.adicionar_item(comanda.numero, "Coca Cola", "bebida", 2)
    restaurante.adicionar_item(comanda.numero, "Suco", "bebida", 1)

    # exemplo de remoção de item antes do fechamento
    restaurante.remover_item(comanda.numero, "Suco")

    print(f"Itens da comanda: {comanda.itens.para_lista_python()}")
    print(f"Valor total antes do pagamento: R$ {comanda.valor_total():.2f}")

    # fechamento da comanda + pagamento
    pagamento = restaurante.fechar_comanda(comanda.numero, forma_pagamento="PIX")
    print(f"Pagamento registrado: {pagamento}")


def main():
    estoque = montar_estoque_inicial()
    restaurante = Restaurante(estoque)

    # simula alguns atendimentos completos
    for _ in range(3):
        simular_atendimento(restaurante)
        print("-" * 40)

    # relatórios
    relatorio_vendas(restaurante.pagamentos)
    relatorio_consumo(restaurante.historico_comandas.para_lista_python())

    # persistência não volátil com pickle
    salvar_dados(restaurante, CAMINHO_DADOS)
    print(f"\nDados salvos em '{CAMINHO_DADOS}'.")

    # exemplo de recarregamento
    restaurante_carregado = carregar_dados(CAMINHO_DADOS)
    print(f"Dados recarregados: {len(restaurante_carregado.pagamentos)} pagamentos no histórico.")


if __name__ == "__main__":
    main()
