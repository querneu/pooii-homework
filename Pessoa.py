# Criação de Classe pai Pessoa com atributos nome e sobrenome
class Pessoa:

    # Metodo construtor vazio para criação de instancias vazias
    def init(self):
    def __init__(self):
        super().__init__()
        pass 

    # GetNome para retornar o valor de nome
    def getNome(self):
        return self._nome

    # SetNome para Inserir o valor de nome
    def setNome(self,nome):
        self._nome = nome

    # GetSobrenome para retornar o valor de sobrenome
    def getSobrenome(self):
        return self._sobrenome

    # SetSobrenome para Inserir o valor de sobrenome
    def setSobrenome(self,sobrenome):
        self._sobrenome = sobrenome