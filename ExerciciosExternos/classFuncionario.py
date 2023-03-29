class Funcionario:

    def __init__(self,nome,salario):

        self._nome = nome
        self._salario = salario

    def getBonificacao(self):

        bonificacao =  self._salario * 0.15

        return bonificacao

    