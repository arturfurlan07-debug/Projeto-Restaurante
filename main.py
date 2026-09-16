import random

from controle.estoque import Estoque
from controle.restaurante import Restaurante
from dados.gerador_aleatorio import gerar_estoque_inicial, gerar_nome_cliente, NOMES_REFEICOES, NOMES_BEBIDAS
from dados.arquivo_dados import salvar_dados, carregar_dados
from relatorios.relatorios import relatorio_vendas, relatorio_consumo

CAMINHO_ARQUIVO = "arquivos_salvos/restaurante.pkl"
FORMAS_PAGAMENTO = ["PIX", "Cartão", "Dinheiro"]


def montar_estoque():
    estoque = Estoque()
    for produto in gerar_estoque_inicial():
        estoque.adicionar_produto(produto)
    return estoque


def simular_atendimento(restaurante):
    nome_cliente = gerar_nome_cliente()
    comanda = restaurante.abrir_comanda(nome_cliente)
    print(f"\nComanda aberta: {comanda}")

    # inclusão de uma ou mais refeições, escolhidas aleatoriamente
    quantidade_refeicoes = random.randint(1, 2)
    refeicoes_escolhidas = random.sample(NOMES_REFEICOES, quantidade_refeicoes)
    for nome_refeicao in refeicoes_escolhidas:
        restaurante.adicionar_item(comanda.numero, nome_refeicao, "refeicao", 1)

    # inclusão de uma ou mais bebidas, também aleatórias
    quantidade_bebidas = random.randint(1, 2)
    bebidas_escolhidas = random.sample(NOMES_BEBIDAS, quantidade_bebidas)
    for nome_bebida in bebidas_escolhidas:
        quantidade = random.randint(1, 2)
        restaurante.adicionar_item(comanda.numero, nome_bebida, "bebida", quantidade)

    # demonstra a remoção de item antes do fechamento (só se sobrar
    # pelo menos 1 item depois, pra comanda não fechar vazia)
    itens_atuais = comanda.itens.obter_todos()
    if len(itens_atuais) > 1:
        item_escolhido = random.choice(itens_atuais)
        restaurante.remover_item(comanda.numero, item_escolhido.nome)
        print(f"Item removido antes de fechar: {item_escolhido.nome}")

    print("Itens finais da comanda:")
    for item in comanda.itens.obter_todos():
        print(f"  - {item}")
    print(f"Valor total: R$ {comanda.calcular_total():.2f}")

    # fechamento da comanda: baixa estoque + registra pagamento
    forma_pagamento = random.choice(FORMAS_PAGAMENTO)
    pagamento = restaurante.fechar_comanda(comanda.numero, forma_pagamento)
    print(pagamento)


def main():
    estoque = montar_estoque()
    restaurante = Restaurante(estoque)

    # simula 3 atendimentos completos, populando o sistema
    for numero_atendimento in range(3):
        simular_atendimento(restaurante)

    print()
    relatorio_vendas(restaurante.pagamentos)
    relatorio_consumo(restaurante.historico_comandas.obter_todos())

    # salva os dados de forma não volátil (pickle)
    salvar_dados(restaurante, CAMINHO_ARQUIVO)
    print(f"\nDados salvos em '{CAMINHO_ARQUIVO}'.")

    # carrega de novo, provando que a persistência funciona
    restaurante_recarregado = carregar_dados(CAMINHO_ARQUIVO)
    total_no_historico = restaurante_recarregado.historico_comandas.tamanho
    print(f"Comandas no histórico depois de recarregar o arquivo: {total_no_historico}")


if __name__ == "__main__":
    main()
