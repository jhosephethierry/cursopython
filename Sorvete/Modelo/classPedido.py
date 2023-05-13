from Controle.classConexao import Conexao

class Pedido:
    
    def __init__(self, id, idCliente, idProduto, quantidade, valorTotal, timestamp):

        self._id = id
        self._idCliente = idCliente
        self._idProduto = idProduto
        self._quantidade = quantidade
        self._valorTotal = valorTotal
        self._timestamp = timestamp

    def sqlInserirPedido(self):

        sql = f'''
        
        INSERT INTO "Pedidos"
        VALUES(default, '{self._idCliente}', '{self._idProduto}', '{self._quantidade}', '{self._valorTotal}', default)
        
        '''

        return sql

    def inserirPedido():

        print("Cadastro de Pedido")

        pedido = Pedido(None, input("Digite o id do cliente. "), input("Digite o id do produto. "), input("Digite a quantidade. "), None, None)