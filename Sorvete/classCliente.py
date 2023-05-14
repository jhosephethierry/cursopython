from classConexao import Conexao

class Cliente:

    def __init__(self, id, nome) -> None:
        
        self._id = id
        self._nome = nome

    def inserirCliente(self):

        print("Cadastro de Cliente")

        self._nome = input("Digite o nome do cliente. ")

        sql = f'''
        
        INSERT INTO "Clientes"
        Values(default, '{self._nome}')

        '''

        if Conexao.manipularBanco(sql):

            print(f"Novo cliente inserido com sucesso!")

        else:

            print("Ocorreu um erro ao inserir o cliente!")
    