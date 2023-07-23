class ContaBancaria:

    def __init__(self,titular,saldo):
        self.titular = titular   
        self.saldo = saldo
    
    def depositar (self):
        valordeposito = float(input('Digite o valor:'))
        return valordeposito
    
    def saque (self):
        valorsaque = float(input('Digite o valor do saque:'))
        return valorsaque
    
    def consultarsaldo (self):
        self.saldo = saldo
        return self.saldo
    
titular1 = ContaBancaria('Maria',0)

titular1.depositar()
titular1.saque()
print(titular1.consultarsaldo())
    
    