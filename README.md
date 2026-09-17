# Projeto Restaurante Nagasima.

Sistema que simula o atendimento de um restaurante: comandas, estoque,
<<<<<<< HEAD
pagamentos e relatórios, usando **estruturas de dados próprias** — sem
usar list, pilha ou fila prontas do Python para as estruturas do problema.
=======
pagamentos e relatórios, usando **estruturas de dados próprias**
>>>>>>> b6fe801a774c8f621b706f38f9f0a8fa7f5f2242

## Estrutura de pastas

```
restaurante/
├── colecoes/          # estruturas de dados genéricas, feitas do zero
│   ├── no.py              -> Nó usado pelas estruturas encadeadas
│   ├── lista.py            -> Lista Encadeada (itens da comanda, estoque)
│   ├── fila.py             -> Fila FIFO (comandas abertas)
│   └── pilha.py            -> Pilha LIFO (histórico de comandas fechadas)
├── entidades/          # classes de dados do domínio
│   ├── produto.py
│   ├── item_comanda.py
│   ├── comanda.py
│   └── pagamento.py
├── controle/            # regras de negócio
│   ├── estoque.py         -> controla produtos, baixa priorizando vencimento
│   └── restaurante.py     -> junta comandas, estoque e pagamentos
├── dados/
│   ├── gerador_aleatorio.py -> gera dados com Faker
│   └── arquivo_dados.py     -> salva/carrega com pickle
├── relatorios/
│   └── relatorios.py       -> relatório de vendas e de consumo
├── arquivos_salvos/     -> onde o .pkl é salvo (gerado ao rodar)
└── main.py              -> simula o atendimento completo
```

## Por que usei essas estruturas?

- **Lista**: guarda os itens de uma comanda (podem ser adicionados e
  removidos livremente antes do fechamento) e os produtos do estoque.
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
>>>>>>> b6fe801a774c8f621b706f38f9f0a8fa7f5f2242
