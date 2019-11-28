from Pessoa import Pessoa
from Aluno import Aluno
from Professor import Professor

pessoa = Pessoa()
aluno = Aluno()
professor = Professor()

def main():
    pessoa.setNome(input("Digite o nome da pessoa: "))
    pessoa.setSobrenome(input("Digite o sobrenome da pessoa: "))
    print("Nome da pessoa:" + pessoa.getNome())
    print("Sobrenome da pessoa:" + pessoa.getSobrenome())

    aluno.setNome(input("Digite o nome do aluno: "))
    aluno.setSobrenome(input("Digite o sobrenome do aluno: "))
    aluno.setMatricula(input("Digite a matricula do aluno: "))
    print("Nome da aluno:" + aluno.getNome())
    print("Sobrenome da aluno:" + aluno.getSobrenome())
    print("Matricula do aluno:" + aluno.getMatricula())


    professor.setNome(input("Digite o nome do professor: "))
    professor.setSobrenome(input("Digite o sobrenome do professor: "))
    professor.setCodigo(input("Digite o codigo do professor: "))
    print("Nome da professor:" + professor.getNome())
    print("Sobrenome da professor:" + professor.getSobrenome())
    print("Código do professor:" + professor.getCodigo())

if __name__ == '__main__':
    main()