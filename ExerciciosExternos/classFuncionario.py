class Funcionario:

    def __init__(self,nome,salario):

        self._nome = nome
        self._salario = salario

    def getBonificacao(self):

        bonificacao =  self._salario * 0.1

        print(f'o valor da bonificacao é R$ {bonificacao}')


# final do programa
        
funcionario = Funcionario('José',7000)

funcionario.getBonificacao()

    