from src.crianca import Crianca

class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.filaDeEspera = []
        self.criancasPulando = []
        self.caixa = 0
        self.conta = {}

    def getFilaDeEspera(self):
        return self.filaDeEspera

    def getCriancasPulando(self):
        return self.criancasPulando

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for crianca in self.criancasPulando:
            if crianca.getNome() == nome:
                return self.conta[nome]
        return None

    def entrarNaFila(self, crianca: Crianca):
        for c in self.filaDeEspera:
            if c.getNome() == crianca.getNome():
                return False
        for c in self.criancasPulando:
            if c.getNome() == crianca.getNome():
                return False
        self.filaDeEspera.append(crianca)
        return True
    def entrar(self):
        if len(self.criancasPulando) < self.limiteMax and self.filaDeEspera:
            crianca = self.filaDeEspera[0]
            self.filaDeEspera = self.filaDeEspera[1:]
            self.criancasPulando.append(crianca)
            if crianca.getNome() in self.conta.keys():
                self.conta[crianca.getNome()] += 2.50
            else:
                self.conta[crianca.getNome()] = 2.50
            self.caixa += 2.50
            return True
        else:
            return False

    def sair(self):
        if self.criancasPulando:
            crianca = self.criancasPulando[0]
            self.filaDeEspera.append(crianca)
            self.criancasPulando = self.criancasPulando[1:]
            return True
        return False

    def papaiChegou(self, nome):
        for crianca in self.criancasPulando:
            if crianca.getNome() == nome:
                self.conta[crianca.getNome()]= 0
                return True
        for crianca in self.filaDeEspera:
            if crianca.getNome() == nome:
                self.conta[crianca.getNome()] = 0
                return True
        return False

    def fechar(self):
        self.criancasPulando.clear()
        self.filaDeEspera = []
        return True

