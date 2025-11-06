# Importa a biblioteca textwrap, que é usada para formatar textos
# (neste caso, para remover a indentação do menu).
import textwrap


def menu():
    """
    Função que exibe o menu de opções e captura a escolha do usuário.
    """
    # Define o texto do menu usando uma string de múltiplas linhas (heredoc).
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    
    # textwrap.dedent() remove os espaços em branco no início de cada linha do menu.
    # input() exibe o menu e aguarda o usuário digitar uma opção.
    return input(textwrap.dedent(menu_texto))


def depositar(saldo, valor, extrato, /):
    """
    Função para processar um depósito.
    O / indica que todos os parâmetros antes dele (saldo, valor, extrato) 
    são 'posicionais-apenas', ou seja, não podem ser passados com nome (ex: depositar(valor=100)).
    """
    # Verifica se o valor do depósito é positivo.
    if valor > 0:
        # Adiciona o valor ao saldo.
        saldo += valor
        # Registra a operação no extrato.
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        # Se o valor for negativo ou zero, exibe uma mensagem de erro.
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o novo saldo e o extrato atualizado.
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função para processar um saque.
    O * indica que todos os parâmetros depois dele (saldo, valor, etc.)
    são 'nomeados-apenas' (keyword-only), ou seja, devem ser passados com nome (ex: sacar(saldo=100, valor=50)).
    """
    # Cria variáveis booleanas para facilitar a leitura das condições.
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    # Verifica se o valor do saque é maior que o saldo.
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    # Verifica se o valor do saque é maior que o limite por saque.
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    # Verifica se o número de saques já atingiu o limite diário.
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    # Se todas as verificações passarem e o valor for positivo...
    elif valor > 0:
        # Subtrai o valor do saldo.
        saldo -= valor
        # Registra a operação no extrato.
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        # Incrementa o contador de saques realizados.
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    # Se o valor do saque for negativo ou zero.
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o saldo e o extrato atualizados.
    # !! ATENÇÃO: Existe um bug aqui no seu código original.
    # Você altera 'numero_saques' mas não o retorna.
    # A função 'main' não saberá que 'numero_saques' mudou.
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    """
    Função para exibir o extrato da conta.
    'saldo' é posicional-apenas, 'extrato' é nomeado-apenas.
    """
    print("\n================ EXTRATO ================")
    # Operador ternário: se 'extrato' estiver vazio, exibe a mensagem; senão, exibe o extrato.
    print("Não foram realizadas movimentações." if not extrato else extrato)
    # Exibe o saldo atual formatado.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """
    Função para cadastrar um novo usuário (cliente).
    """
    # Pede o CPF e armazena.
    cpf = input("Informe o CPF (somente número): ")
    # Verifica se o CPF já existe na lista de usuários.
    usuario = filtrar_usuario(cpf, usuarios)

    # Se 'filtrar_usuario' retornar um usuário, significa que ele já existe.
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return  # Encerra a função.

    # Se o CPF for novo, pede os dados restantes.
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Adiciona o novo usuário (em formato de dicionário) à lista 'usuarios'.
    # Isso modifica a lista 'usuarios' que foi passada como argumento (mutação).
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    """
    Função auxiliar para buscar um usuário pelo CPF na lista de usuários.
    """
    # Usa 'list comprehension' para criar uma nova lista contendo apenas os usuários com o CPF informado.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    # Retorna o primeiro usuário da lista (se ela não estiver vazia), ou 'None' (se estiver vazia).
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Função para criar uma nova conta bancária, vinculando-a a um usuário.
    """
    # Pede o CPF do usuário para vincular à conta.
    cpf = input("Informe o CPF do usuário: ")
    # Busca o usuário na lista de usuários.
    usuario = filtrar_usuario(cpf, usuarios)

    # Se o usuário for encontrado...
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        # Retorna um dicionário representando a nova conta.
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    # Se o usuário não for encontrado, a conta não pode ser criada.
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    # Retorna 'None' (implicitamente), que será tratado na função 'main'.


def listar_contas(contas):
    """
    Função para exibir os detalhes de todas as contas criadas.
    """
    # Itera sobre cada dicionário de 'conta' na lista 'contas'.
    for conta in contas:
        # Cria uma string de múltiplas linhas formatada com os dados da conta.
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        # Usa textwrap.dedent para exibir a string formatada corretamente.
        print(textwrap.dedent(linha))


def main():
    """
    Função principal que executa o programa.
    """
    # Define constantes do sistema.
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # Inicializa as variáveis de estado.
    # !! ATENÇÃO: Este é o principal problema do código.
    # 'saldo', 'limite', 'extrato' e 'numero_saques' são globais.
    # Eles não pertencem a nenhuma conta específica.
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # Loop principal do programa.
    while True:
        # Exibe o menu e obtém a opção do usuário.
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            # Chama 'depositar' e atualiza as variáveis globais.
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            # Chama 'sacar' e atualiza as variáveis.
            # !! BUG: 'numero_saques' não é atualizado aqui.
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            # Exibe o extrato global.
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            # Cria um novo usuário (modifica a lista 'usuarios').
            criar_usuario(usuarios)

        elif opcao == "nc":
            # Gera um número de conta sequencial simples.
            numero_conta = len(contas) + 1
            # Tenta criar uma conta.
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            # Se a conta foi criada com sucesso (não é 'None')...
            if conta:
                # Adiciona a conta à lista de contas.
                contas.append(conta)

        elif opcao == "lc":
            # Lista todas as contas criadas.
            listar_contas(contas)

        elif opcao == "q":
            # Se a opção for 'q' (quit), quebra o loop.
            break

        else:
            # Mensagem para opções inválidas.
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Executa a função principal para iniciar o programa.
main()