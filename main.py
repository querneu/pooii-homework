# Importando as classes necessárias
from Pessoa import Pessoa
from Aluno import Aluno
from Professor import Professor

# instanciando os objetos das classes importadas
pessoa = Pessoa()
aluno = Aluno()
professor = Professor()

# Metodo principal de execução do código
def main():

    # Inserindo o valor de nome e sobrenome via input
    pessoa.setNome(input("Digite o nome da pessoa: "))
    pessoa.setSobrenome(input("Digite o sobrenome da pessoa: "))

    # retornando o valor pelos gets do objeto importado
    print("Nome da pessoa:" + pessoa.getNome())
    print("Sobrenome da pessoa:" + pessoa.getSobrenome())

    # Inserindo o valor de nome e sobrenome via input
    aluno.setNome(input("Digite o nome do aluno: "))
    aluno.setSobrenome(input("Digite o sobrenome do aluno: "))
    aluno.setMatricula(input("Digite a matricula do aluno: "))

    # retornando o valor pelos gets do objeto importado
    print("Nome da aluno:" + aluno.getNome())
    print("Sobrenome da aluno:" + aluno.getSobrenome())
    print("Matricula do aluno:" + aluno.getMatricula())

    # Inserindo o valor de nome e sobrenome via input
    professor.setNome(input("Digite o nome do professor: "))
    professor.setSobrenome(input("Digite o sobrenome do professor: "))
    professor.setCodigo(input("Digite o codigo do professor: "))

    # retornando o valor pelos gets do objeto importado
    print("Nome da professor:" + professor.getNome())
    print("Sobrenome da professor:" + professor.getSobrenome())
    print("Código do professor:" + professor.getCodigo())

    # definindo que se o nome do arquivo for main ele será
    # tratado como execução primaria
if __name__ == '__main__':
    main()