# Trabalho de Programação Orientada a Objetos 2
### Status: [![Build Status](https://travis-ci.com/querneu/pooii-homework.svg?branch=master)](https://travis-ci.com/querneu/pooii-homework)


# Diagrama UML
![alt text](https://raw.githubusercontent.com/querneu/pooii-homework/master/diagrama-de-classe.png)


# Classes

A tabela abaixo descreve cada classe criada

| Classe    | Descrição |
| ------    | ------    |
| main      | Classe principal de execução do código |
| Pessoa    | Classe Pai |
| Aluno     | Classe filha, herda nome e sobrenome, possui Matricula |
| Professor | Classe filha, herda nome e sobrenome, possui Codigo|
|pytest     | Classe de teste de execução unitária requerida para utilização do [travis] |
### Classe Pessoa:
- ### Atributos
    * [Nome]- Atributo do tipo String que recebe o nome de [Pessoa]
    * [Sobrenome] - Atributo do tipo String que recebe o sobrenome de [Pessoa]
- ### Metodos
    * [getNome]- Metodo que retorna o valor inserido em [self._nome]
    * [getSobrenome] - Metodo que retorna o valor inserido em [self._sobrenome]
    * [setNome]- Metodo que insere valor em [self._nome]
    * [setSobrenome] - Metodo que insere valor em [self._sobrenome]

A classe [Pessoa] é a classe pai contendo nome e sobrenome que são atributos comuns para [Aluno] e [Professor]

### Classe Aluno:
- ### Atributos
    * [Nome]- Atributo do tipo String que recebe o nome de [Aluno], herdado de [Pessoa]
    * [Sobrenome] - Atributo do tipo String que recebe o sobrenome de [Aluno], herdado de [Pessoa]
    * [Matricula] - Atributo do tipo Integer que recebe o numero da matrícula de [Aluno], herdado de [Pessoa]
- ### Metodos
    * [getMatricula]- Metodo que retorna o valor inserido em [self._matricula], herdado de [Pessoa]
    * [setMatricula] - Metodo que insere valor em [self._matricula], herdado de [Pessoa]

A classe [Aluno] é uma das classes filhas que herdam os atributos de [Pessoa], possui [Matricula]

### Classe Professor:
- ### Atributos
    * [Nome]- Atributo do tipo String que recebe o nome de [Professor], herdado de [Pessoa]
    * [Sobrenome] - Atributo do tipo String que recebe o sobrenome de [Professor], herdado de [Pessoa]
    * [Codigo] - Atributo do tipo Integer que recebe o numero do Código de [Professor], herdado de [Pessoa]
- ### Metodos
    * [getCodigo]- Metodo que retorna o valor inserido em [self._codigo], herdado de [Pessoa]
    * [setCodigo] - Metodo que insere valor em [self._codigo], herdado de [Pessoa]

A classe [Professor] é uma das classes filhas que herdam os atributos de [Pessoa], possui [Codigo]


### Equipe
|                                         | Integrante|
| ------                                  | ------    |
| Nome                                    | Lucas Soares Leite |
| Matrícula                               | 91604374 |
| Curso                                   | Sistemas de informação |
| Principais responsabilidades no projeto | Realizar o desenvolvimento do projeto, incluindo UML, testes, build, documentação e vídeo|

### Video

        Em breve!

**Obrigado pelo Semestre!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [travis]: <https://travis-ci.com/>
   [pessoa]: <https://github.com/querneu/pooii-homework/blob/master/Pessoa.py>
   [aluno]: <https://github.com/querneu/pooii-homework/blob/master/Aluno.py>
   [professor]:<https://github.com/querneu/pooii-homework/blob/master/Professor.py>
   [Nome]: <https://github.com/querneu/pooii-homework/blob/024426bad1b47248c61693e4889b244e0ab7b0af/Pessoa.py#L1>
   [self._nome]: <https://github.com/querneu/pooii-homework/blob/024426bad1b47248c61693e4889b244e0ab7b0af/Pessoa.py#L9>
   [Sobrenome]: <https://github.com/querneu/pooii-homework/blob/024426bad1b47248c61693e4889b244e0ab7b0af/Pessoa.py#L1>
   [self._sobrenome]: <https://github.com/querneu/pooii-homework/blob/024426bad1b47248c61693e4889b244e0ab7b0af/Pessoa.py#L14>
   [matricula]:<https://github.com/querneu/pooii-homework/blob/master/Aluno.py#L3>
   [codigo]:<https://github.com/querneu/pooii-homework/blob/master/Professor.py#L3>
   [getNome]: <https://github.com/querneu/pooii-homework/blob/master/Pessoa.py#L6>
   [getSobrenome]: <https://github.com/querneu/pooii-homework/blob/master/Pessoa.py#L11>
   [getMatricula]: <https://github.com/querneu/pooii-homework/blob/master/Aluno.py#L5>
   [getCodigo]: <https://github.com/querneu/pooii-homework/blob/master/Aluno.py#L5>
   [setNome]: <https://github.com/querneu/pooii-homework/blob/master/Pessoa.py#L8>
   [setSobrenome]: <https://github.com/querneu/pooii-homework/blob/master/Pessoa.py#L13>
   [setMatricula]: <https://github.com/querneu/pooii-homework/blob/master/Aluno.py#L8>
   [setCodigo]: <https://github.com/querneu/pooii-homework/blob/master/Aluno.py#L8>
   
   [self._codigo]:<https://github.com/querneu/pooii-homework/blob/master/Professor.py#L9>
   [self._matricula]:<https://github.com/querneu/pooii-homework/blob/master/Aluno.py#L9>
   
 
