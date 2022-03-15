"""
EXERCÍCIO FINAL DE SEÇÃO:
1- crie uma classe Pessoa que recebe no método construtor: nome, idade, cpf e o tempo de trabalho como atributos da pessoa
Também, declare um método chamado aposentadoria e outro com o nome salario_aposentadoria, ambos são implementados pelas
classes Filhas. Dicas, utilize os conceitos aprendidos em poliformismo.
Após isso, crie duas classes: Homem e mulher, as duas classes Filhas de Pessoa. Dentro da classe Homem desenvolva o método
de aposentadoria que irá testar se o objeto possui idade maior ou igual a 65 e tempo de trabalho maior ou igual a 15 anos,
caso positivo, retorne 'VocÊ pode se aposentar', caso contrário, 'Ainda não atingiu os requisitos para se aposentar'. Também
implemente o método salário_aposentadoria que irá testar se o objeto possui idade maior ou igual a 65 e um tempo de trabalho
maior ou igual a 15 anos, caso positivo, retorne o salário de direito pela seguinte equação:
    salário = 1000 + (tempo_trabalho - 15) * 200
Caso contrário, retorne 'Você não pode se aposentar'. Faça o mesmo procedimento na classe Mulher, porém ao invés da idade
ser 65, deverá ser 60.
Utilize Doctests pra fazer os tests na classe Homem e Unittests na classe mulher. Utilize o método TDD.

"""

class Pessoa:

    def __init__(self, nome, idade, cpf, tempo_trabalho):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__tempo_trabalho = tempo_trabalho

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def tempo_trabalho(self):
        return self.__tempo_trabalho

    def aposentadoria(self):
        raise NotImplementedError('Metodo especifico de criterio para a Subclasse')

    def salario_aposentadoria(self):
        raise NotImplementedError('Metodo especifico de criterio para a Subclasse')

class Homem(Pessoa):

    def __init__(self, nome, idade, cpf, tempo_trabalho):
        super().__init__(nome, idade, cpf, tempo_trabalho)

    def aposentadoria(self):
        """
        Irá testar se o objeto tem idade maior ou igual a 65 anos e tempo de trabalho maior ou igual a 15 anos

        >>> maicon = Homem('Maicon', 67, 123456, 20)
        >>> maicon.aposentadoria()
        'Voce pode se aposentar'

        >>> flavio = Homem('Flavio', 45, 132456, 22)
        >>> flavio.aposentadoria()
        'Ainda nao atingiu os requisitos para se aposentar'
        """
        if self.idade >= 65 and self.tempo_trabalho >= 15:
            return 'Voce pode se aposentar'
        else:
            return 'Ainda nao atingiu os requisitos para se aposentar'

    def salario_aposentadoria(self):
        """
        Verifica quanto é o salário do aposentado

        >>> maicon = Homem('Maicon', 65, 123456, 20)
        >>> maicon.salario_aposentadoria()
        2000

        >>> flavio = Homem('Flavio', 61, 132456, 22)
        >>> flavio.salario_aposentadoria()
        'Voce nao pode se aposentar'
        """
        if self.idade >= 65 and self.tempo_trabalho >= 15:
            salario = 1000 + (self.tempo_trabalho - 15) * 200
            return salario
        return 'Voce nao pode se aposentar'

class Mulher(Pessoa):

    def __init__(self, nome, idade, cpf, tempo_trabalho):
        super().__init__(nome, idade, cpf, tempo_trabalho)

    def aposentadoria(self):
        if self.idade >= 60 and self.tempo_trabalho >= 15:
            return 'Voce pode se aposentar'
        else:
            return 'Ainda nao atingiu os requisitos para se aposentar'

    def salario_aposentadoria(self):
        if self.idade >= 60 and self.tempo_trabalho >= 15:
            salario = 1000 + (self.tempo_trabalho - 15) * 200
            return salario
        return 'Voce nao pode se aposentar'