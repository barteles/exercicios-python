"""
EXERCÍCIO DE MÉTODOS MÁGIOS:
1- Um escritor de livros pretente escrever e lançar edições para atingir a quantia de 1 milhão de reais. Simplesmente
por esse motivo, crie uma classe que receberá esse método construtor o nome do livro e o número de páginas. Além disso,
também deve ser criado um atributo no construtor para a edição do livro, que será atualizado em uma unidade a cada livro
que for publicado. Por fim, utilize radint() para gerar um valor entre 0 e 500 mil, representando a arrecadação das vendas,
o ultimo atributo do construtor. Crie o método mágico __repr__ para representar o nome do livro e a edição. Ainda,
utilize __len__ para determinar o número de páginas de cada livro. Por fim, verifique se o valor total de arrecadaçao
atingiu 1 milhão de reais.

RESULTADO;
from random import randint as ri

class Livros:

    def __init__(self, nome, numPg, edicao, valorArre):
        self.nome = nome
        self.numPg = numPg
        self.edicao = edicao
        self.valorArre = valorArre

    def __repr__(self):
        return f'{self.nome} - Edição: {self.edicao}'

    def __len__(self):
        return self.numPg

livro1 = Livros('Old Mans War', 251, 1, ri(0,500000))
livro2 = Livros('Saga The Witcher, livro 1', 230, 5, ri(0,500000))
livro3 = Livros('Memórias Póstumas de Brás Cubas', 130, 10, ri(0,500000))

print(livro1)
print(livro2)
print(livro3)

print(f'\nLivro 1: {len(livro1)} páginas')
print(f'Livro 2: {len(livro2)} páginas')
print(f'Livro 3: {len(livro3)} páginas')

print(f'\nValor arrecadado pelo livro 1: R${livro1.valorArre}')
print(f'Valor arrecadado pelo livro 2: R${livro2.valorArre}')
print(f'Valor arrecadado pelo livro 3: R${livro3.valorArre}')

valorTotal = livro1.valorArre + livro2.valorArre + livro3.valorArre
if valorTotal > 1000000:
    print('\nParabéns! Você é um milionário!')
else:
    print('\nAinda não chegou no 1 milhão. Tente criar mais livros')
print(f'Valor Arrecadado: R${valorTotal}')


#_______________________________________________________________________________________________________________________

EXERCÍCIO PROPRIEDADES:
2- Crie uma classe contendo atributos públicos e privados representando objetos pessoais. Após isso, crie uma propriedade
para cada atributo privado. Instancie um objeto e faça acesso a todos os atributos.Utilize também o setter, para alterar
algum valor.

RESULTADO:
class Objeto:

    def __init__(self, videoGame, senhaCelular, dinheiro, camisa, livro):
        self.__videoGame = videoGame
        self.__senhaCelular = senhaCelular
        self.__dinheiro = dinheiro
        self.camisa = camisa
        self.livro = livro

    @property   #retorna atributos privados como se fossem públicos
    def videogame(self):
        return f'Primo(a), estou brincando com seu {self.__videoGame}'

    @property
    def senhaCelular(self):
        return f'Descobri a sua senha: {self.__senhaCelular}'

    @property
    def dinheiro(self):
        return f'me empresta seus {self.__dinheiro} reais aí'

    @dinheiro.setter    #altero valores dentro de um atributo privado
    def dinheiro(self, quantidade):
        self.__dinheiro = quantidade

joao = Objeto('Playstation 2', 'joaozinho007', 135, 'adidas 11', 'Cálculo 1')
maria = Objeto('XBOX 360', 'maria_nas', 800, 'Garfield', 'Estruturas moleculares')

#imprimindo todos os atributos
print(joao.videogame)
print(joao.senhaCelular)
print(joao.dinheiro)
joao.dinheiro = 3550    #alterei o valor do dinheiro e imprimi os dois para verificar se deu certo
print(joao.dinheiro)
print(joao.camisa)
print(joao.livro)

print('\n')
print(maria.videogame)
print(maria.senhaCelular)
print(maria.dinheiro)
maria.dinheiro = 250
print(maria.dinheiro)
print(maria.camisa)
print(maria.livro)

#_______________________________________________________________________________________________________________________

EXERCÍCIOS HERÂNÇA E MÉTODO SUPER.
3- Desenvolva o sistema de um controle universal para uma casa. O controle deve ser a classe-MÃE, que contém o método
liga/desliga e é herdada por 3 classes (equipamentos controlados): ar-condicionado, micro-ondas e televisão, que controlam
respectivamente, temperatura, tempo e volume em métodos dentro das classes. Além disso, os métodos construtores das Classes
Filhas recebem a variável controlada em seu valor atual, por exemplo 'temperaturaAtual'.
Obs.:Utilize também propriedades para realizar acesso aos atributos.

RESULTADO:
class Controle:
    ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

class Arcondicionado(Controle): #classe filha de classe Controle (mãe)

    def __init__(self, temperaturaAtual):
        self.__temperaturaAtual = temperaturaAtual

    def controle_temperatura(self, temperatura):    #aqui define a temperatura do âmbiente
        self.__temperaturaAtual = temperatura

    @property       #aqui só irá acessar nosso atributo
    def temperaturaAtual(self):
        return f'Temperatura atual: {self.__temperaturaAtual}'

class Microondas(Controle):

    def __init__(self, tempoAtual):
        self.__tempoAtual = tempoAtual

    def controle_tempo(self, tempo):
        self.__tempoAtual = tempo

    @property
    def tempoAtual(self):
        return f'Tempo atual: {self.__tempoAtual}'

class Televisao(Controle):

    def __init__(self, volumeAtual):
        self.__volumeAtual = volumeAtual

    def controle_volume(self, volume):
        self.__volumeAtual = volume

    @property
    def volumeAtual(self):
        return f'Volume atual é: {self.__volumeAtual}'

arc = Arcondicionado(45)
mic = Microondas(60)
tv = Televisao(85)

print(arc.ligado)
arc.liga_desliga()
print(arc.ligado)
print(arc.temperaturaAtual)
arc.controle_temperatura(35)
print(arc.temperaturaAtual)
print('\n')

print(mic.ligado)
mic.liga_desliga()
print(mic.ligado)
print(mic.tempoAtual)
mic.controle_tempo(15)
print(mic.tempoAtual)
print('\n')

print(tv.ligado)
tv.liga_desliga()
print(tv.ligado)
print(tv.volumeAtual)
tv.controle_volume(40)
print(tv.volumeAtual)


#_______________________________________________________________________________________________________________________

EXERCÍCIO HERÂNÇA MULTIPLA:
4-Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome como parâmetro. Estas classes devem herdar de outras
duas chamadas 'Carnívoros' e 'Herbivoros', que possuem dois métodos cada ('caçar_animal' e 'comer_carne' para 'Carnivoros';
'procurar_arvore' e 'comer_folhas' para 'Herbivoros') e herdam de uma Superclasse chamada 'Animal', na qual possui os
métodos 'andar' e 'correr'. Por fim, instancie dois objetos, da classe 'Homem' e da classe 'Urso', e execute todos os métodos
OBS.: Crie um método para as classes 'Homem' e 'Urso' representando uma ação característica de cada, por exemplo ler um livro
para o homem e hibernar para o urso.

RESULTADO:
class Animal:

    def andar(self):
        print('Andando...')

    def correr(self):
        print('Correndo...')


class Carnivoro(Animal):

    def cacar_animal(self):
        print('Caçando animal...')

    def comer_carne(self):
        print('Comendo carne....')


class Herbivoros(Animal):

    def procurar_arvore(self):
        print('Procurando árvore...')

    def comer_folha(self):
        print('Comendo folhas...')


class Homem(Carnivoro, Herbivoros): #herança direta de Carnívoro e Herbivoros, porém herança indireta de Animal
    def __init__(self,nome):    #pois, tanto Carnívoro quanto Herbívoros herdam de Animal
        self.__nome = nome

    def lendo_livro(self):
        print('Lendo livro...')

class Urso(Carnivoro, Herbivoros):
    def __init__(self,nome):
        self.__nome = nome

    def hibernar(self):
        print('Hibernando')

homem = Homem('André')
homem.lendo_livro()
homem.andar()
homem.procurar_arvore()
homem.correr()
homem.cacar_animal()
homem.comer_carne()
homem.comer_folha()

print('\n')
ze = Urso('Zé colméia')
ze.andar()
ze.hibernar()
ze.procurar_arvore()
ze.correr()
ze.cacar_animal()
ze.comer_carne()
ze.comer_folha()


#_______________________________________________________________________________________________________________________


EXERCÍCIO SOBRE POLIFORMISMO
5- Crie uma superclasse chamada 'FormaGeometrica', que possui um método 'calcula-área' e recebe o nome de uma figura
geométrica em seu método construtor. Após isso, crie duas subclasses ('Areaquadrado' e 'Areacirculo') que herdam de
'Formageometrica' e calculam a área de sua respectiva forma. O método nas classes filhas deve ter o nome 'calcula_area',
igual em sua classe mãe.

RESULTADO:
import math
class Formageometrica:

    def __init__(self, nome):
        self.__nome = nome

    def calcula_area(self):
        if self.__nome == 'quadrado':
            print(f"Área do quadrado: {(float(input('Digite o lado do quadrado: '))) ** 2} m²")
        elif self.__nome == 'circulo':
            print(f"Área do circulo: {((float(input('Digite o raio do circulo: '))) ** 2) * math.pi}m²")

class Areaquadrado(Formageometrica):

    def calcula_area(self):
        print(f"Área: {(float(input('Digite o lado do quadrado: '))) ** 2} m²")


class Areacirculo(Formageometrica):

    def calcula_area(self):
        print(f"Área: {((float(input('Digite o raio do circulo: '))) ** 2) * math.pi} m²")


quadrado = Areaquadrado('quadrado')     #devo respeitar o __init__ da Superclasse, ou seja, passar o parâmetro pedido
quadrado.calcula_area()

circulo = Areacirculo('circulo')
circulo.calcula_area()  #O resultado sairá do método da Superclasse, pois essa possui prioridade ante as subclasses


#_______________________________________________________________________________________________________________________

EXERCICIO FINAL DE SEÇÃO:
6- Crie uma superclase chamada 'Pessoa' que recebe como atributos nome, cpf, salário. APós isso, construa a classe filha:
'Funcionário', que possui o método sem parâmetros chamado 'Promoção', que apenas acrescenta 10% no salário a algum
funcionário. Por sua vez, a classe 'Funcionario' deve ser a classe mãe de duas outras classes: 'Gerente' e 'Estagiario',
e ambos precisam ter o atributo 'código' em seu método construtor. Além disso, o gerente precisa do atributo 'numEstagiarios'
representando a quantidade de funcionarios que ele é responsável. Ainda, na classe gerente deve haver um método que possibilite
a alteração do código dos estagiários, sendo que estagiários não tem acesso a troca de código. Instancie 3 estagiários e 1
gerente. Dê promoção para os dois primeiros estagiarios e para o gerente.
OBS.: Utilize também um método mágico para representar as classes 'Estagiário' e 'Gerente', e propriedades para acessar
os atributos de 'Pessoa'.

"""

class Pessoa:

    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, aumento):
        self.__salario = aumento

class Funcionario(Pessoa):
    def promocao(self):
        self.salario *= 1.1     #como cada objeto é único, não precisa de índices para separar os objetos

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, codigo, numEstagiario, codigoEstag):
        super().__init__(nome, cpf, salario)    #só irei usar isso quando pedir os parâmetros iguais ao código construtor
        self.__codigo = codigo                  #da Superclasse
        self.__numEstagiario = numEstagiario
        self.__codigoEstag = codigoEstag

    def mudar_codigo(self, novoCodigo):
        self.__codigoEstag = novoCodigo

    def __repr__(self):
        return f'Sou o(a) gerente: {self.nome}, recebo {round(self.salario)} reais e quero um café'

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, codigo):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo

    def __repr__(self):
        return f'Sou o(a) estagiário(a): {self.nome}, recebo {round(self.salario)} reais e tenho que levar café na ' \
               f'administração'

gerente  = Gerente('Pablo', 12345678900, 12000, 3,  'gege123', 'es1234')
estagiario1 = Estagiario('João', 1234567911, 400, 'es1234')
estagiario2 = Estagiario('Maria', 1234567912, 400, 'es1234')
estagiario3 = Estagiario('Ana', 1234567913, 400, 'es1234')

print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())
print(estagiario3.__repr__())

estagiario1.promocao()
estagiario2.promocao()
gerente.promocao()
print('\n')
print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())
print(estagiario3.__repr__())
