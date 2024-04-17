saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def menu():
    menu = """
    
████████████████████████████████
█▄─▄─▀██▀▄─██▄─▀█▄─▄█─▄▄▄─█─▄▄─█
██─▄─▀██─▀─███─█▄▀─██─███▀█─██─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    opcao = input(menu)
    return opcao

def deposito():
    global saldo, extrato

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    ver_extrato()

def saque():
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUES

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    ver_extrato()

def ver_extrato():
    global saldo, extrato

    print("\n\n")
    print(" EXTRATO ".center(40, '='))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("="*40)
    input("\nPrecione qualquer tecla para sair")
    limpar()

def limpar():
    import os

    system_name = os.uname()

    if system_name.sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

while True:
    opcao = menu()

    if opcao == "d":
        deposito()

    elif opcao == "s":
        saque()

    elif opcao == "e":
        ver_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
