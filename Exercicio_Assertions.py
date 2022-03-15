"""
EXERCÍCIO DE TESTES SOBRE ASSERTIONS
1- Aplique assert`s no código abaixo e descreva o que o programa faz:

RESULTADO:
 - O programa descreve uma classe que cria uma conta corrente para as pessoas, recebendo atributos nome, numero da conta
 e saldo inicial, por padrão (caso não seja informado) igual a zero. Os atributos são privados e por isso é necessário
 propriedades para acessa-los, por fim, há um método de depósito e saque que altera o valor do saldo inicial, e com isso
 instanciando dois objetos.

 class ContaCorrente:

    def __init__(self,nome, num_conta,saldo =0.0):
        assert type(nome) is str, 'O nome deve ser do tipo String'
        assert type(num_conta) is int, 'O número da conta deve ser do tipo inteiro'
        assert type(saldo) is float, 'O saldo deve ser FLOAT para realizar operações bancárias'
        assert saldo >= 0, 'O saldo deve ser maior ou igual a zero'
        self.__nome = nome
        self.__num_conta = num_conta
        self.__saldo = saldo

    @property
    def nome(self):
        return self.__nome
    @property
    def num_conta(self):
        return self.__num_conta
    @property
    def saldo(self):
        return self.__saldo

    def deposito(self, valor):
        assert valor >= 0, 'O valor de depósito deve ser positivo'
        assert type(valor) is float, 'O valor deve ser do tipo float para realizar operações bancárias'
        self.__saldo = self.__saldo + valor

    def saque(self, valor):
        assert valor >= 0, 'O valor de saque deve ser positivo'
        assert type(valor) is float, 'O valor deve ser do tipo float para realizar operações bancárias'
        assert self.__saldo >= valor, f'Dinheiro insuficiente, você tem disponível R$ {self.__saldo} para saque'
        self.__saldo = self.__saldo - valor

pessoa = ContaCorrente('Sandro', 12345)
pessoa2 = ContaCorrente('Vanessa', 67891,500.0)

assert isinstance(pessoa, ContaCorrente), 'Pessoa não encontrada no banco de dados'
assert isinstance(pessoa2, ContaCorrente), 'Pessoa não encontrada no banco de dados'

x======================================================================================================================x

EXERCÍCIO DE UNITTEST
2-Rafael deseja entrar na onda fitness, para isso colocou várias metas como, acordar cedo, definir um tempo de exercício,
definir dias de descanso e qual esporte irá praticar. Para isso aplique o método TDD para criar e testar as próximas
tres funções:
 a) acordar_cedo: Essa função recebe a hora que ele acordou como parâmetro e testa se acordou após as 6 horas, caso
 afirmativo retorne 'Tente novamente amanhã', caso contrário, 'Você é um guerreiro'

 b) tempo_exercicio: essa função recebe a quantidade de horas exercitadas e o peso (kg) de Rafael, caso o tempo seja
 inferior a 2 horas, utilize pass, caso contrário, reduza 1 kg do peso e retorne o valor.

 c) tem_exercicio: Função que reconhece se é um dia de descanso ou não, recebe como parãmetro o esporte que irá praticar
 no dia, caso recebe a string 'Descanso' retorne False (Para mostrar que hoje não há exercício), caso contrário retorne
 True.

RESULTADO:
def acordar_cedo(horario):
    if horario > 6:
        return 'Tente novamente amanhã'
    return 'Você é um guerreiro'

def tempo_exercicio(tempo, peso):
    if tempo > 2:
        peso -= 1
        return peso
    pass


def tem_execicio(esporte):
    if esporte == 'Descanso':
        return False
    return True


X======================================================================================================================X

EXERCÍCIO SETUP AND TEARDOWN

3- Crie uma classe chamada Tatu que recebe em seu método construtor o nome dele, dentro da classe implemente os seguintes
métodos:
 - comer: Retorna 'sou o NOME e estou comendo pizza'
 - beber: Retorna 'sou o NOME e estou bebendo suco'
 - acasalar: Retornar 'sou o NOME e quero um filhote'
Faça os testes para cada um dos métodos e crie dois setUp: Bola e Napoleão e use um ou outro para aplicar os testes.
Além disso, aplique o tearDown para apresentar 'Teste concluido'.
Obs.: Utilize o método TDD.

RESULTADO:
class Tatu:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        return f'sou o {self.__nome} e estou comendo pizza'

    def beber(self):
        return f'sou o {self.__nome} e estou bebendo suco'

    def acasalar(self):
        return f'sou o {self.__nome} e quero um filhote'


________________________________________________________________________________________________________________________

EXERCÍCIO DOCTESTES
4- Crie um programa representando uma calculadora que realiza as operações de multiplicação, divisão, potência e fatorial
com até dois números. Receba do usuário a operação desejada e os números escolhidos por ele. Implemente uma função para
cada operação matemática utilizando os Doctestes, por fim, faça o tratamento de eroos com try/except/else/finally.
OBS.: Utilize o método TDD.

RESULTADO:
def multiplicacao(a,b):
    '''
    Define a multiplicação de 2 números a e b.
    >>> multiplicacao(2,3)
    6
    '''
    
    return a * b

def divisao(a,b):
    '''
    Define a divisão de dois números inteiros a e b.
    >>> divisao(20,5)
    4.0
    '''

    return a/b

def potencia(a,b):
    '''
    Define a potência de a elevado à b.
    >>> potencia(3,2)
    9
    '''

    return a ** b

def fatorial(a):
    '''
    Define o fatorial de um número
    >>> fatorial(5)
    120
    '''

    b = a  - 1
    while b !=0:
        a = a * b
        b -= 1
    return a

try:
    op = int(input('Digite 1- multiplicação\n2- Divisão\n3- Potência\n4-Fatoração'
                   '\nOpção: '))
except ValueError:
    print('Apenas números são aceitos!')
else:
    try:
        if op ==1:
            resultado = multiplicacao(int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')))
            print(f'A operação escolhida foi multiplicação e o resultado foi: {resultado}')
        elif op == 2:
            resultado = divisao(int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')))
            print(f'A operação escolhida foi divisao e o resultado foi: {resultado}')
        elif op == 3:
            resultado = potencia(int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')))
            print(f'A operação escolhida foi potencia e o resultado foi: {resultado}')
        elif op == 4:
            resultado = fatorial(int(input('Digite o primeiro valor: ')))
            print(f'A operação escolhida foi fatorial e o resultado foi: {resultado}')
        else:
            print('Operação inválida')
    except ValueError:
        print('Digite somente números inteiros')
finally:
    print('Programa finalizado')
    
    
________________________________________________________________________________________________________________________



"""

