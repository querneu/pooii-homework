from Pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self):
        pass
    def getCodigo(self):
        return self._codigo
    
    def setCodigo(self, codigo):
        self._codigo = codigo