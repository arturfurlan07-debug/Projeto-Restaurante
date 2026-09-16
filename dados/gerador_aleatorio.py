import random
from datetime import timedelta

from faker import Faker

from entidades.produto import Produto

fake = Faker("pt_BR")

NOMES_REFEICOES = ["Feijoada", "Frango Grelhado", "Estrogonofe", "Salada Caesar", "Lasanha"]
NOMES_BEBIDAS = ["Coca Cola", "Suco", "Água"]


def gerar_estoque_inicial():
    """
    Cria um produto pra cada item do cardápio, com preço, datas e
    quantidade aleatórios usando a biblioteca Faker.
    """
    produtos = []
    for nome in NOMES_REFEICOES + NOMES_BEBIDAS:
        data_compra = fake.date_time_between(start_date="-15d", end_date="now")
        dias_ate_vencer = random.randint(2, 20)
        data_vencimento = data_compra + timedelta(days=dias_ate_vencer)
        preco_compra = round(random.uniform(2.0, 20.0), 2)
        preco_venda = round(preco_compra * random.uniform(1.5, 2.5), 2)
        quantidade = random.randint(10, 50)

        produto = Produto(nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade)
        produtos.append(produto)
    return produtos


def gerar_nome_cliente():
    return fake.name()
