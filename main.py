# VERSÃO 2 - OTIMIZADA COM FUNÇÕES

def exibir_menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    menu = """
================ MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[q]\tSair
=> """
    return input(menu)

def depositar(saldo, extrato):
    """
    Realiza a operação de depósito.
    Recebe o saldo e o extrato, solicita o valor do depósito,
    atualiza os dados e os retorna.
    """
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nOperação falhou! O valor informado é inválido.")
    except ValueError:
        print("\nOperação falhou! Por favor, insira um valor numérico.")
    
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    Recebe todos os dados da conta como argumentos nomeados (keyword-only).
    Retorna o saldo, extrato e número de saques atualizados.
    """
    try:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print(f"\nOperação falhou! Saldo insuficiente. (Saldo: R$ {saldo:.2f})")
        elif excedeu_limite:
            print(f"\nOperação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso!")
        else:
            print("\nOperação falhou! O valor informado é inválido.")
    except ValueError:
        print("\nOperação falhou! Por favor, insira um valor numérico.")
        
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    Recebe o saldo como argumento posicional e o extrato como argumento nomeado.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================")

def main():
    """Função principal que executa o sistema bancário."""
    # Constantes
    LIMITE_SAQUES = 3
    
    # Variáveis de estado da conta
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    # Loop principal
    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break
        
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
