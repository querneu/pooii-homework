from .Pessoa import Pessoa

class Professor:
    def __init__(self, Pessoa, codigo):
        self._nome = Pessoa._nome
        self._sobrenome = Pessoa._sobrenome
        self._codigo = codigo
    
    def getCodigo(self):
        return self._codigo
    
    def setCodigo(self, codigo):
        self._codigo = codigo