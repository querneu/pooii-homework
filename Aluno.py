# Importe da classe pai para aluno receber atributos de herança.
from Pessoa import Pessoa

# Criação de classe aluno já instanciando pessoa.
class Aluno(Pessoa):        
    def __init__(self):
        pass

    # Metodo getMatricula para retornar o valor da matricula solicitada.
    def getMatricula(self):
        return self._matricula
    
    # Metodo serMatricula para inserir o valor da matricula.
    def setMatricula(self,matricula):
        self._matricula = matricula