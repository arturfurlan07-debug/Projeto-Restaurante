import random
from datetime import timedelta

from faker import Faker

from modelos.produto import Produto

fake = Faker("pt_BR")

NOMES_REFEICOES = ["Feijoada", "Frango Grelhado", "Estrogonofe", "Salada Caesar", "Lasanha"]
NOMES_BEBIDAS = ["Coca Cola", "Suco", "Água"]


def gerar_produtos_estoque(quantidade=10):
    """Gera uma lista de produtos (refeições e bebidas) com dados aleatórios."""
    produtos = []
    nomes = NOMES_REFEICOES + NOMES_BEBIDAS
    for nome in nomes[:quantidade] if quantidade <= len(nomes) else nomes:
        data_compra = fake.date_time_between(start_date="-15d", end_date="now")
        data_vencimento = data_compra + timedelta(days=random.randint(2, 20))
        preco_compra = round(random.uniform(2.0, 20.0), 2)
        preco_venda = round(preco_compra * random.uniform(1.5, 2.5), 2)
        produtos.append(
            Produto(
                nome=nome,
                preco_compra=preco_compra,
                preco_venda=preco_venda,
                data_compra=data_compra,
                data_vencimento=data_vencimento,
                quantidade=random.randint(10, 50),
            )
        )
    return produtos


def gerar_nome_cliente():
    return fake.name()
