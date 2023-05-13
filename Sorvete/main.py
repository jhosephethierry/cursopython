from Modelo.classFuncoes import Funcoes
import psycopg2

while True:

    try:
        print('''Sorvetes Sorriso
        
        Escolha uma opção no menu abaixo.

            1. Inserir Novo Cliente
            2. Inserir Novo Produto
            3. Inserir Novo Pedido
            0. Sair
        
        ''')   

        op = input("Digite uma das opções. ")
        
        match op:

            case "1":
                inserirNovoCliente()
            
            case "2":
                inserirNovoProduto()

            case "3":
                inserirNovoPedido()

            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Opção inválida!")

        input("Digite Enter para continuar.")

    except(Exception, psycopg2.Error) as error:
        print(error)
        s