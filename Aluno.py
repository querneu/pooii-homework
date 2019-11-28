from Pessoa import Pessoa
class Aluno(Pessoa):        
    def __init__(self):
        pass
    def getMatricula(self):
        return self._matricula
    
    def setMatricula(self,matricula):
        self._matricula = matricula