# 🏦 Projeto Sistema Bancário em Python

Este é um projeto de console desenvolvido em Python que simula as operações básicas de um sistema bancário. O foco do projeto é aplicar conceitos de programação procedural, separando a lógica em funções e gerenciando o estado do sistema em memória através de listas e dicionários.

Este projeto foi desenvolvido como um exercício prático para demonstrar habilidades em lógica de programação e estruturação de dados em Python.

---

## 🎯 Funcionalidades

O sistema permite gerenciar usuários, contas e realizar operações financeiras básicas para a conta que estiver selecionada:

### Gerenciamento de Usuários e Contas
* **[nu] Novo Usuário:** Cadastra um novo cliente com nome, CPF e endereço.
* **[nc] Nova Conta:** Cria uma nova conta corrente vinculada a um usuário (pelo CPF).
* **[lc] Listar Contas:** Exibe os detalhes de todas as contas cadastradas.
* **[sc] Selecionar Conta:** Permite escolher uma conta existente para realizar as operações de depósito, saque e extrato.

### Operações Bancárias
* **[d] Depositar:** Adiciona um valor positivo ao saldo da conta selecionada.
* **[s] Sacar:** Retira um valor da conta selecionada. Esta operação respeita três regras:
    1.  O valor não pode exceder o saldo em conta.
    2.  O valor não pode exceder o limite por saque (ex: R$ 500,00).
    3.  O usuário não pode exceder o limite de saques diários (ex: 3 saques).
* **[e] Extrato:** Exibe o histórico de transações (depósitos e saques) e o saldo atual da conta selecionada.
* **[q] Sair:** Encerra o programa.

---

## 🛠️ Conceitos e Tecnologias Aplicadas

* **Linguagem:** Python 3
* **Estrutura de Dados:**
    * **Listas:** Para armazenar o conjunto de usuários e de contas.
    * **Dicionários:** Para estruturar os dados de cada usuário e de cada conta (incluindo saldo, extrato, limites, etc.).
* **Programação Procedural:** O código é modularizado em funções, onde cada função tem uma responsabilidade única (ex: `depositar()`, `criar_usuario()`, `selecionar_conta()`).
* **Gerenciamento de Estado:** O estado do sistema (dados de usuários, contas, saldos) é gerenciado em memória e passado como argumento para as funções.
* **Entrada e Saída:** Interação com o usuário via terminal (`input()` e `print()`).
