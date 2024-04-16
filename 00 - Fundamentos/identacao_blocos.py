from time import sleep   

def sacar(valor, saldo):
    if saldo >= valor:
        print("Valor sacado\n")
        saldo -= valor

        print(f"-Saldo atual é: {saldo}")

    else:
        print("Erro, você tentou sacar um valor acima do contido no saldo")
        print(f"-Seu saldo é: {saldo}")

    print("Obrigado por ser nosso cliente, tenha um ótimo dia!")
    sleep(3)
    limpar()
    return saldo

def limpar():
    import os

    system_name = os.uname()

    if system_name.sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

saldo_atual = 500
novo_saldo = 0

while True:
    print(f"Seu saldo é: {saldo_atual}\n")

    saque = int(input("Digite o valor que deseja sacar: "))

    novo_saldo = sacar(saque, saldo_atual)

    opt = " "
    while opt not in "SN":
        opt = str(input("Deseja sair? [S/N]: ")).strip().upper()[0]

    if opt == 'S':
        print(f"Seu saldo restante é de: {novo_saldo}")
        limpar()
        sleep(3)
        break
    else:
        saldo_atual = novo_saldo
        limpar()
        sleep(1)
        