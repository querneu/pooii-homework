class Pessoa:
    def __init__(self):
        super().__init__()
        pass 

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome

    def getSobrenome(self):
        return self._sobrenome
    def setSobrenome(self,sobrenome):
        self._sobrenome = sobrenome