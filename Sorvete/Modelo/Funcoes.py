from Controle.classConexao import Conexao

from Modelo.classCliente import Cliente
from Modelo.classProduto import Produto
from Modelo.classPedido import Pedido

import psycopg2



def inserirCliente():

    print("Cadastro de Cliente")

    cliente = Cliente(None, input("Digite o nome do cliente. "))

    Conexao.manipularBanco(cliente.sqlInserirCliente())

    print("Novo cliente inserido com sucesso!")



def inserirProduto():

    print("Cadastro de Produto")

    produto = Produto(None, input("Digite o nome do produto. "), input("Digite o peso. "), input("Digite o preço. "), input("Digite o estoque. "))

    Conexao.manipularBanco(produto.sqlInserirProduto())

    print("Novo produto inserido com sucesso!")



def inserirPedido():

    print("Cadastro de Pedido")

    pedido = Pedido(None, input("Digite o id do cliente. "), input("Digite o id do produto. "), input("Digite a quantidade. "), None, None)