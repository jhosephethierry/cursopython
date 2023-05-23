from classConexao import Conexao

class Pomar:

    def __init__(self, id, fruta, peso, estoque) -> None:
        
        self._id = id
        self._fruta = fruta
        self._peso = peso
        self._estoque = estoque
        self._datacolheita = None
        
    def sqlInserirFruta(self):

        sql = f'''
        
        INSERT INTO "Pomar"
        Values(default, '{self._fruta}', '{self._peso}', '{self._estoque}')

        '''

        return sql
    
    def sqlEscolherFruta(self):

        sql = f'''
        
        UPDATE "Pomar"
        SET
        "Fruta" = '{self._frut}'
        WHERE "Id" = '{self._id}'

        '''

        return sql
    
    def sqlAtualizarEstoque(self):

        sql = f'''
        
        UPDATE "Pomar"
        SET
        "Estoque" = '{self._estoque}'
        WHERE "Id" = '{self._id}'

        '''

        return sql