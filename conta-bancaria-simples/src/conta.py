class Conta:
    def __init__(self, numero:int, saldo:float):
        self.limite= 100
        self.extrato = []
        self.saldo = saldo
        self.numero = numero
        self.operacoes = 0

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo + self.limite

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -=valor
                self.extrato.append(-valor)
            elif self.saldo + self.limite >= valor:
                self.limite -= (valor- self.saldo)
                self.saldo =0
                self.extrato.append(-valor)
            else:
                return False
            return True
        else:
            return False

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(valor)
            self.operacoes +=1
            if self.saldo > 0:
                self.limite = 100
            return True
        else:
            return False
    def transferir(self, destino, valor:float):
        if destino and valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
            elif self.saldo + self.limite >= valor:
                self.limite -= (valor - self.saldo)
                self.saldo = 0
                destino.depositar(-valor)
            else:
                return False
            destino.depositar(valor)
            self.extrato.append(-valor)
            self.operacoes +=1
            return True
        else:
            return False

    def verExtrato(self):
        return self.extrato[-10:]