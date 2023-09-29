from src.pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        self.minutos = 0
        self.pessoas = 0

    def getPessoa(self):
        return self.pessoas

    def getTempo(self):
        return self.minutos

    def getPotencia(self):
        return -1

    def subir(self, pessoa: Pessoa):
        return False

    def descer(self):
        return False

    def colocarTempo(self, tempo: int):
        return False

    def dirigir(self, tempo: int):
        return True

    def buzinar(self):
        return None
