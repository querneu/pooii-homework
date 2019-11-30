# Importe da classe pai para aluno receber atributos de herança
from Pessoa import Pessoa
# Criação de classe aluno já instanciando pessoa
class Professor(Pessoa):
    def __init__(self):
        pass
    
    # Metodo getMatricula para retornar o valor da matricula solicitada
    def getCodigo(self):
        return self._codigo
    
    # Metodo serMatricula para inserir o valor da matricula
    def setCodigo(self, codigo):
        self._codigo = codigo