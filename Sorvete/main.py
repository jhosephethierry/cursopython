from Modelo.classFuncoes import Funcoes
import psycopg2

while True:

    try:
        print('''Sorvetes Sorriso
        
        Escolha uma opção no menu abaixo.

            1. Inserir Cliente
            2. Inserir Produto
            3. Inserir Pedido
            4. Vizualizar Clientes
            5. Vizualizar Produtos
            6. Vizualizar Pedidos
            0. Sair
        
        ''')   

        op = input("Digite uma das opções. ")
        
        match op:

            case "1":
                inserirCliente()
            
            case "2":
                inserirProduto()

            case "3":
                inserirPedido()

            case "4":
                visualizarClientes()

            case "5":
                visualizarProdutos()

            case "6":
                visualizarPedidos()

            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Digite uma opção válida.")

        input("Digite Enter para continuar.")

    except(Exception, psycopg2.Error) as error:
        print(error)
