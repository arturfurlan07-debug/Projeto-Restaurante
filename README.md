# Projeto Restaurante Nagasima.

Sistema que simula o atendimento de um restaurante: comandas, estoque,
pagamentos e relatórios, usando **estruturas de dados próprias**

## Estrutura de pastas

```
restaurante/
├── estruturas/       # estruturas de dados genéricas, implementadas do zero
│   ├── no.py             -> Nó usado pelas estruturas encadeadas
│   ├── lista_encadeada.py -> Lista Encadeada (itens da comanda, estoque)
│   ├── fila.py            -> Fila FIFO (comandas abertas, ordem de chegada)
│   └── pilha.py           -> Pilha LIFO (histórico de comandas fechadas)
├── modelos/          # entidades do domínio (dados puros)
│   ├── produto.py
│   ├── item_pedido.py
│   ├── comanda.py
│   └── pagamento.py
├── servicos/         # regras de negócio
│   ├── estoque.py        -> gerencia produtos, baixa priorizando vencimento
│   └── restaurante.py    -> orquestra comandas, estoque e pagamentos
├── gerador/
│   └── gerador_dados.py  -> gera dados aleatórios com Faker
├── persistencia/
│   └── persistencia.py   -> salva/carrega dados com pickle
├── relatorios/
│   └── relatorios.py     -> relatório de vendas e de consumo
├── dados/             -> onde o .pkl é salvo (gerado em runtime)
└── main.py            -> simula o atendimento completo
```

## Por que usei essas estruturas?

- **Lista Encadeada**: usada para os itens de uma comanda (refeições/bebidas
  podem ser adicionados e removidos livremente antes do fechamento) e para
  o estoque, mantido **ordenado por data de vencimento**, garantindo que os
  produtos mais velhos sejam sempre consumidos primeiro.
- **Fila (FIFO)**: representa as comandas abertas na ordem em que os
  clientes chegaram — faz sentido semântico com o problema real.
- **Pilha (LIFO)**: histórico de comandas fechadas, para consulta rápida
  das últimas comandas pagas (mais recente primeiro).

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```

## Autor
 Artur Furlan — Trabalho da disciplina Estrutura de Dados / Linguagem de Programação 2 — Fatec Rio Claro.
