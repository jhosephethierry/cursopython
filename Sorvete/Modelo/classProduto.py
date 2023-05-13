from Controle.classConexao import Conexao

class Produto:

    def __init__(self, id, nome, peso, preço, estoque,) -> None:
        
        self._id = id
        self._nome = nome
        self._peso = peso
        self._preço = preço
        self._estoque = estoque

    def sqlInserirProduto(self):

        sql = f'''
        
        INSERT INTO "Produtos"
        Values(default, '{self._nome}', '{self._peso}', '{self._preço}', '{self._estoque}')

        '''

        return sql
    
    def sqlAtualizarProduto(self):

        sql = f'''

        UPDATE "Produtos"
        SET
        "Nome" = '{self._nome}', "Peso" = '{self._peso}', "Preço" = '{self._preço}', "Estoque" = '{self._estoque}'
        WHERE "Id" = {self._id}
        
        '''

        return sql
    
    def inserirProduto():

        print("Cadastro de Produto")

        produto = Produto(None, input("Digite o nome do produto. "), input("Digite o peso. "), input("Digite o preço. "), input("Digite o estoque. "))

        Conexao.manipularBanco(produto.sqlInserirProduto())

        print("Novo produto inserido com sucesso!")