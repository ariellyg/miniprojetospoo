class Carro:

    def __init__(self):
        self.tanque = 0
        self.passageiros = 0
        self.quilometragem = 0

    def getPassageiros(self):
       return self.passageiros

    def getCombustivel(self):
        return self.tanque

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            self.passageiros += 1
            return True
        else:
            return False

    def desembarcar(self):
        if self.passageiros <= 2 and self.passageiros != 0:
            self.passageiros -= 1
            return True
        else:
            return False

    def dirigir(self, distancia):
        if self.passageiros > 0 and self.tanque > 0:
            consumo = distancia
            if consumo <= self.tanque:
                self.tanque -= consumo
                self.quilometragem += distancia
                return True
            else:
                self.quilometragem+= self.tanque
                self.tanque = 0
                return 'voce esta sem combustivel'
    def abastecer(self, quantidade):
        if self.tanque + quantidade < 100:
            self.tanque += quantidade
            return 'quantidade nao chegou ao limite'
        if self.tanque + quantidade == 100:
            self.tanque += quantidade
            return 'valor max atingido'
        else:
            return quantidade-100


