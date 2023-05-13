from Controle.classConexao import Conexao

class Cliente:

    def __init__(self, id, nome) -> None:
        
        self._id = id
        self._nome = nome

    def sqlInserirCliente(self):

        sql = f'''
        
        INSERT INTO "Clientes"
        Values(default, '{self._nome}')

        '''

        return sql
    
    def inserirCliente():

        print("Cadastro de Cliente")

        cliente = Cliente(None, input("Digite o nome do cliente. "))

        Conexao.manipularBanco(cliente.sqlInserirCliente())

        print("Novo cliente inserido com sucesso!")

    