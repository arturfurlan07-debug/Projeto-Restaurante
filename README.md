# Projeto Restaurante Nagasima.

Sistema que simula o atendimento de um restaurante para a Fatec com comandas, estoque, pagamentos e relatórios.

## Estrutura do projeto 

```text
restaurante/
├── colecoes/                  # Estruturas de dados genéricas, feitas do zero
│   ├── no.py                  # Nó usado pelas estruturas encadeadas
│   ├── lista.py               # Lista Encadeada (itens da comanda e estoque)
│   ├── fila.py                # Fila FIFO (comandas abertas)
│   └── pilha.py               # Pilha LIFO (histórico de comandas fechadas)
│
├── entidades/                 # Classes de dados do domínio
│   ├── produto.py
│   ├── item_comanda.py
│   ├── comanda.py
│   └── pagamento.py
│
├── controle/                  # Regras de negócio
│   ├── estoque.py             # Controla produtos e baixa priorizando vencimento
│   └── restaurante.py         # Integra comandas, estoque e pagamentos
│
├── dados/                     # Geração e persistência de dados
│   ├── gerador_aleatorio.py   # Gera dados utilizando Faker
│   └── arquivo_dados.py       # Salva e carrega dados utilizando pickle
│
├── relatorios/                # Geração de relatórios
│   └── relatorios.py          # Relatórios de vendas e consumo
│
├── arquivos_salvos/           # Arquivos .pkl gerados durante a execução
│
├── main.py                    # Executa a simulação completa do atendimento
└── .gitignore                 # Arquivos e pastas ignorados pelo Git
```

Por que usei essas estruturas?

-**Lista**: guarda os itens de uma comanda (podem ser adicionados e removidos livremente antes do fechamento) e os produtos do estoque.
  A busca do produto certo na hora de dar baixa sempre prioriza o que
  está mais perto do vencimento, percorrendo a lista manualmente.
- **Fila (FIFO)**: comandas abertas, na ordem em que os clientes chegam.
- **Pilha (LIFO)**: histórico de comandas fechadas — a última paga fica
  sempre no topo, fácil de consultar.

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```
=======
 Artur Furlan — Trabalho da disciplina Estrutura de Dados / Linguagem de Programação 2 — Fatec Rio Claro.
