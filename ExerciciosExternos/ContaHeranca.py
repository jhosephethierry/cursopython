class Conta:

    def __init__(self,saldo):

        self._saldo = saldo

    # outros metodos

    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa

class ContaCorrente(Conta):
    
    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self,valor):
        self._saldo += valor - 0.10

class ContaPoupanca(Conta):
    
    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa * 3


conta = Conta("123-4", "Jose", 1000)
contacorrente = Conta("123-4", "Jose", 1000)
contapoupanca = Conta("123-6", "Maria", 2000)

conta.atualiza(0.01)
contacorrente.atualiza(0.01)
contapoupanca.atualiza(0.01)

print(conta.saldo)
print(contacorrente.saldo)
print(contapoupanca.saldo)

