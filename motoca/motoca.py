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
        if self.pessoas is None:
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
            if self.pessoas.getIdade() <= 10:
               pilotou = tempo
            else:
                pilotou = 0
            self.minutos -= pilotou
            return pilotou
        elif self.pessoas is not None and self.minutos > 0:
            pilotou = self.minutos
            self.minutos = 0
            return pilotou
        else:
            return False
    def buzinar(self):
        if self.pessoas is not None:
            buzina = 'p' + 'e' * self.potencia + 'm'
        else:
            return 'não pode buzinar'

