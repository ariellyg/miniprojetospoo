class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energiaAtual = self.energiaMax
        self.saciedadeAtual = self.saciedadeMax
        self.limpezaAtual = self.limpezaMax
        self.idadeAtual = 0
        self.diamantes = 0
        self.estaVivo = True


    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        return self.estaVivo

    def brincar(self):
        if self.estaVivo:
            self.energiaAtual = max(0,self.energiaAtual - 2)
            self.saciedadeAtual = max(0, self.saciedadeAtual - 1)
            self.limpezaAtual = max(0, self.limpezaAtual -3)
            self.diamantes += 1
            self.idadeAtual +=1
            if self.idadeAtual >= self.idadeMax:
                self.estaVivo = False
                self.idadeAtual = self.idadeMax
            if self.energiaAtual == 0 or self.saciedadeAtual == 0 or self.limpezaAtual == 0:
                self.estaVivo = False
            return True
        else:
            return False

    def comer(self):
        if self.estaVivo:
            self.energiaAtual = max(0, self.energiaAtual - 1)
            self.saciedadeAtual = min(self.saciedadeMax, self.saciedadeAtual + 4)
            self.limpezaAtual =max(0, self.limpezaAtual - 2)
            self.diamantes += 0
            self.idadeAtual += 1
            if self.idadeAtual >= self.idadeMax:
                self.estaVivo = False
                self.idadeAtual = self.idadeMax
            if self.energiaAtual == 0 or self.saciedadeAtual == 0 or self.limpezaAtual == 0:
                self.estaVivo = False
            return True
        else:
            return False

    def dormir(self):
        if self.estaVivo:
            if self.energiaAtual <= self.energiaMax - 5:
                turnos = self.energiaMax - self.energiaAtual
                self.idadeAtual += turnos
                self.energiaAtual = self.energiaMax
                self.saciedadeAtual = max(0, self.saciedadeAtual - 2)
                if self.idadeAtual >= self.idadeMax:
                    self.estaVivo = False
                    self.idadeAtual = self.idadeMax
                if self.energiaAtual == 0 or self.saciedadeAtual == 0 or self.limpezaAtual == 0:
                    self.estaVivo = False
                return True
        return False
    def banhar(self):
        if self.estaVivo:
            self.energiaAtual = max(0, self.energiaAtual-3)
            self.saciedadeAtual =max(0, self.saciedadeAtual - 1)
            self.limpezaAtual = self.limpezaMax
            self.diamantes += 0
            self.idadeAtual += 2
            if self.idadeAtual >= self.idadeMax:
                self.estaVivo = False
                self.idadeAtual = self.idadeMax
            if self.energiaAtual == 0 or self.saciedadeAtual == 0 or self.limpezaAtual == 0:
                self.estaVivo = False
            return True
        else:
            return False