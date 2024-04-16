def menu():
    opt = int(input('''Digite o indice para selecionar a opção desejada
                    
1. Cadastrar produto
2. Listar produtos cadastrados
3. Sair
                    
===Digite sua opção===: '''))
    
    return opt

def cadastro(compras):
    while True:
        produto = str(input("Digite um produto para adcionar na lista de compras: ")).strip().title()
        compras.append(produto)

        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input("Deseja continuar cadastrando? [S/N]: ")).upper().strip()[0]

            if continuar not in 'SN':
                print("Opção inválida tente novamente.")
        
        if continuar == 'N':
            break

def listar(compras):
    for i,v in enumerate(compras):
        print(f'{i} - {v}')
    
    main()

def main():
    compras = []

    while True:
        from time import sleep

        opt = menu()
        
        if opt == 1:
            cadastro(compras)
        elif opt == 2:
            listar(compras)
        elif opt == 3:
            print('Saindo do programa...')
            sleep(3)
            break
        else:
            pass

if __name__ == '__main__':
    main()