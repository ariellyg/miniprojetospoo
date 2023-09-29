from src.pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        self.potencia = potencia
        self.minutos = 0
        self.pessoas = None

    def getPessoa(self):
        return self.pessoas

    def getTempo(self):
        return self.minutos

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoas is None :
            self.pessoas = pessoa
            return True
        else:
            return False


    def descer(self):
        if self.pessoas is not None:
            self.pessoas = None
            return True
        else:
            return False

    def colocarTempo(self, tempo: int):
        if tempo > 0:
            self.minutos += tempo
            return True
        else:
            return False

    def dirigir(self, tempo: int):
        if self.pessoas is not None and self.minutos >= tempo:
            if self.pessoas.getIdade <= 10:
                dirigiu = tempo
            else:
                dirigiu = 0
                self.minutos -= tempo
            return dirigiu
        else:
            return 0
    def buzinar(self):
        if self.pessoas is not None:
            buzina = 'p'
            for i in range(self.potencia):
                buzina += 'e'
                buzina += 'm'
                return buzina
