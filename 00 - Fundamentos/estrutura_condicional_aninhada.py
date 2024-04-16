conta_normal =  False
conta_universitária = False

saldo = 2000
cheque_especial = 450

print(f'''1. Saque conta pf
2. Saque conta universitária''', end="\n\n")

opt = ' '
while opt not in [1,2]:
    opt = int(input("digite o indice da operação desejada: "))

saque = float(input("Digite o valor que deseja sacar: "))

if opt == 1:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque efetuado com cheque especial")
    else:
        print("Saque não realizado, saldo insuficiente!")
elif opt == 2:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saque não realizado, saldo insuficiente!")