from .Pessoa import  Pessoa

class Aluno:
    def __init__(self,Pessoa, matricula):
        self._nome = Pessoa._nome
        self._sobrenome = Pessoa._sobrenome
        self._matricula = matricula
    
    def getMatricula(self):
        return self._matricula
    
    def setMatricula(self,matricula):
        self._matricula = matricula