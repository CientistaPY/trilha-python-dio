# Potência Tech powered by iFood | Ciências de Dados com Python
# Sistema Bancário v2 - Otimizando o Sistema Bancário com Funções Python
# Desafio 2 proposto pelo módulo "Dominando Python para ciencia de Dados" da Digital Innovation One
# Autor: [Luis Pontes]
# Perfil DIO: [https://web.dio.me/users/MAILTOLUISCARLOS]
# GitHub: [https://github.com/CientistaPY]



import textwrap


def menu_principal():
    menu = """\n
    ================ MENU PRINCIPAL ================
    [ui]\tUso interno
    [uc]\tUso de cliente
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def menu_uso_interno():
    menu = """\n
    ================ MENU USO INTERNO ================
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [v]\tVoltar
    => """
    return input(textwrap.dedent(menu))


def menu_uso_cliente():
    menu = """\n
    ================ MENU USO CLIENTE ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [v]\tVoltar
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao_principal = menu_principal()

        if opcao_principal == "ui":
            while True:
                opcao_interno = menu_uso_interno()

                if opcao_interno == "nc":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        contas.append(conta)

                elif opcao_interno == "lc":
                    listar_contas(contas)

                elif opcao_interno == "nu":
                    criar_usuario(usuarios)

                elif opcao_interno == "v":
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

        elif opcao_principal == "uc":
            while True:
                opcao_cliente = menu_uso_cliente()

                if opcao_cliente == "d":
                    valor = float(input("Informe o valor do depósito: "))
                    saldo, extrato = depositar(saldo, valor, extrato)

                elif opcao_cliente == "s":
                    valor = float(input("Informe o valor do saque: "))
                    saldo, extrato = sacar(
                        saldo=saldo,
                        valor=valor,
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_SAQUES,
                    )

                elif opcao_cliente == "e":
                    exibir_extrato(saldo, extrato=extrato)

                elif opcao_cliente == "v":
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

        elif opcao_principal == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
