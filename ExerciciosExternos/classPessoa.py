class Pessoa:
    
    def __init__(self,nome,idade):
        
        self.nome = nome
        self.idade = idade

    def getNome(self):
         self.nome = print(self.nome)
         return self.nome
        

    def getIdade(self):
        self.idade = print(self.idade)
        return self.idade    

pessoa1 = Pessoa('João',25)

pessoa1.getIdade()
pessoa1.getNome()
