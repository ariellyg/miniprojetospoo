class Passageiro:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def ePrioridade(self):
        return self.idade >= 65


    def getNome(self):
        return self.nome