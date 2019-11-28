from Pessoa import Pessoa
from Aluno import Aluno
from Professor import Professor

pessoa = Pessoa()
aluno = Aluno()
professor = Professor()

def test():
    pessoa.setNome("Pessoa")
    pessoa.setSobrenome("Sobrenome Pessoa")
    print("Nome da pessoa:" + pessoa.getNome())
    print("Sobrenome da pessoa:" + pessoa.getSobrenome())

    aluno.setNome("Aluno")
    aluno.setSobrenome("Sobrenome Aluno")
    aluno.setMatricula(123)
    print("Nome da aluno:" + aluno.getNome())
    print("Sobrenome da aluno:" + aluno.getSobrenome())
    print("Matricula do aluno:" + aluno.getMatricula())


    professor.setNome("Professor")
    professor.setSobrenome("Sobrenome Professor")
    professor.setCodigo(321)
    print("Nome da professor:" + professor.getNome())
    print("Sobrenome da professor:" + professor.getSobrenome())
    print("Código do professor:" + professor.getCodigo())

if __name__ == 'test':
    test()