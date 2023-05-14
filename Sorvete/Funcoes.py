from classCliente import Cliente
from classProduto import Produto
from classPedido import Pedido

import psycopg2


def consultarBanco(sql):

    conn = psycopg2.connect(dbname = "Sorvete", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()

    return resultado
    
def manipularBanco(sql):
        
    conn = psycopg2.connect(dbname = "Sorvete", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()

    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()



def visualizarClientes():


    clientes = consultarBanco('''

    SELECT * FROM "Clientes"
    ORDER BY "Id" ASC

    ''')

    if clientes:

        print("Estes são os clientes cadastrados.")

        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]}")

    else:
        
        print("Não há clientes cadastrados.")



def visualizarProdutos():

    produtos = consultarBanco('''

    SELECT * FROM "Produtos"
    ORDER BY "Id" ASC

    ''')

    if produtos:

        print("Estes são os produtos cadastrados.")

        for produto in produtos:
            print(f"{produto[0]} | {produto[1]} | {produto[2]} | {produto[3]} | {produto[4]}")

    else:
        
        print("Não há produtos cadastrados.")



def visualizarPedidos():

    pedidos = consultarBanco('''

    SELECT * FROM "Pedidos"
    ORDER BY "Id" ASC

    ''')

    if pedidos:

        print("Estes são os pedidos cadastrados.")

        for pedido in pedidos:
            print(f"{pedido[0]} | {pedido[1]} | {pedido[2]} | {pedido[3]} | {pedido[4]} | {pedido[5]}")

    else:
        
        print("Não há pedidos cadastrados.")



def inserirCliente():

    print("Cadastro de Cliente")

    cliente = Cliente(None, input("Digite o nome do cliente. "))

    manipularBanco(Cliente.sqlInserirCliente(cliente))

    print("Novo cliente inserido com sucesso!")

    

def inserirProduto():

    print("Cadastro de Produto")

    produto = Produto(None, input("Digite o nome do produto. "), input("Digite o peso. "), input("Digite o preço. "), input("Digite o estoque. "))

    manipularBanco(produto.sqlInserirProduto())

    print("Novo produto inserido com sucesso!")



def inserirPedido():

    print("Cadastro de Pedido")

    pedido = Pedido(None, input("Digite o id do cliente. "), input("Digite o id do produto. "), input("Digite a quantidade. "), None, None)