from classConexao import Conexao

class Pomar:

    def __init__(self, id, fruta, peso, estoque, colheita) -> None:
        
        self._id = id
        self._fruta = fruta
        self._peso = peso
        self._estoque = estoque
        self._datacolheita = colheita
        
    def sqlInserirFruta(self):

        sql = f'''
        
        INSERT INTO "Pomar"
        Values(default, '{self._fruta}', '{self._peso}', '{self._estoque}', '{self._datacolheita}')

        '''

        return sql