from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.qtdNormais = self.capacidade - self.qtdPrioritarios
        self.psgNormais = [None] * self.qtdNormais
        self.psgPrioritarios = [None] * self.qtdPrioritarios

    def getNumeroAssentosPrioritarios(self):
        if self.qtdPrioritarios <= self.capacidade:
            return self.qtdPrioritarios
        else:
            return ' IllegalArgumentException'

    def getNumeroAssentosNormais(self):
        return self.qtdNormais

    def getPassageiroAssentoNormal(self, lugar):
        if lugar >= 0 and lugar < self.qtdNormais:
            return self.psgNormais[lugar]
        else:
            return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if lugar >= 0 and lugar < self.qtdPrioritarios:
            return self.psgPrioritarios[lugar]
        else:
            return None

    def getVagas(self):
        vagasDisponiveis = 0
        for lugar in self.psgPrioritarios:
            if lugar is None:
                vagasDisponiveis += 1
        for lugar in self.psgNormais:
            if lugar is None:
                vagasDisponiveis += 1
        return vagasDisponiveis

    def subir(self, passageiro: Passageiro):
        if passageiro.ePrioridade():
            for a in range(self.qtdPrioritarios):
                if self.psgPrioritarios[a] is None:
                    self.psgPrioritarios[a] = passageiro
                    return True
        for a in range(self.qtdNormais):
            if self.psgNormais[a] is None:
                self.psgNormais[a] = passageiro
                return True

        else:
            for a in range(self.qtdNormais):
                if self.psgNormais[a] is None:
                        self.psgNormais[a] = passageiro
                        return True
            for a in range(self.qtdPrioritarios):
                if self.psgPrioritarios[a] is None:
                        self.psgPrioritarios[a] = passageiro
                        return True

    def descer(self, nome):
        for a in range(self.qtdPrioritarios):
            if self.psgPrioritarios[a] is not None and self.psgPrioritarios[a].getNome() == nome:
                self.psgPrioritarios[a] = None
                return True

        for a in range(self.qtdNormais):
            if self.psgNormais[a] is not None and self.psgNormais[a].getNome() == nome:
                self.psgNormais[a] = None
                return True

        return False

    def toString(self):
        Topic = '['
        for a in range(self.qtdPrioritarios):
            if self.getPassageiroAssentoPrioritario(a):
               Topic += "@" + self.getPassageiroAssentoPrioritario(a).getNome() + ' '
            else:
                Topic += '@ '
        for a in range(self.qtdNormais):
            if self.getPassageiroAssentoNormal(a):
                Topic += '=' + self.getPassageiroAssentoNormal(a).getNome() + ' '
            else:
                Topic += '= '

        Topic += ']'
        return Topic