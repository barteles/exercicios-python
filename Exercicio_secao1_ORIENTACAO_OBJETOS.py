"""
EXERCÍCIOS DE SEÇÃO DE ORIENTAÇÃO VOLTADA À OBJETOS:
1- Crie uma classe chamada Personagem que irá receber como construtor o nome Completo, altura, peso e resistência (0 a 100)
do personagem, além disso, também crie um método que se chama poder que conterá todos os atributos de uma instãncia como privado,
não sendo possível altera-los, sendo eles: magia, persuasão, agilidade e força, cada um avaliada de 0 a 100, por fim, retorne apenas
a soma de todos os pontos fornecidos. Crie 3 objetos personagens e imprima o nome completo e quantidade de poder total
do mais forte.

RESULTADO:
class Personagem:

    def __init__(self, nome_completo, altura, peso, resistencia):
        self.nome_completo = nome_completo
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

    def poder(self, magia, persuasao, agilidade, forca):
        self.__magia = magia
        self.__persuasao = persuasao
        self.__agilidade = agilidade
        self.__forca = forca
        return magia + persuasao + agilidade + forca

dict_poder = {}
Kratos = Personagem('Kratos', 1.85, 90, 80)
dict_poder[Kratos.nome_completo] = Kratos.poder(100, 10, 50, 90)

Chief = Personagem('Master Chief', 2.3, 130, 75)
dict_poder[Chief.nome_completo] = Chief.poder(0,40, 70, 90)

Sheppard = Personagem('Johnn Sheppard', 1.80, 80, 60)
dict_poder[Sheppard.nome_completo] = Sheppard.poder(70, 80, 50, 65)

print(dict_poder)
#print(Kratos.__dict__)  #retorna um dicionário com todos os atributos de um objeto
#print(Chief.__dict__)
#print(Sheppard.__dict__)

maior = 0
nome = ''

for chave, valor in dict_poder.items(): #deve vir com o .items() pois ele retorna valores de chave e elemento ao mesmo tempo
    if maior < valor:
        maior = valor
        nome = chave
print(f'O mais forte é {nome} com {maior} pontos de poder')


#_______________________________________________________________________________________________________________________

2- Crie uma classe Robo para controlar o objeto R2D2 com os seguintes métodos:
 - Construtor: Recebe como atributo a bateria que varia entre 0 e 100 e cria um atributo de instância chamado estado que
 apresenta se o robô está ligado ou não.
 - liga_desliga: Quando esse método é chamado o robo passa a ser ligado caso esteja desligado e vice-versa
 - movimento: Recebe como atributo uma string, que representa qual lado o robô irá andar e decresce o atributo bateria
 em 10 para cada execução desse método.
 - controle_energia: Imprime os atributos estado e bateria atualizados do robô.
Crie uma interface de menu para o usuário decidir o que irá fazer com o Robo, ou seja, qual método irá acessar. Faça o tratamento
de erros com try/except/Else/Finally. trate também as condiçoes especiais como bateria zerada o que irá acontecer com o
seu R2D2? Dentre outros, fica a cargo do programador.

RESULTADO:
class Robo:


    def __init__(self, bateria):
        self.estado = 'Desligado'
        self.bateria = bateria

    def liga_desliga(self):
        if self.bateria  == 0:
            print('\nRobô está sem bateria, carregue-o')
            self.estado = 'Desligado'
        else:
            if self.estado == 'Desligado':
                self.estado = 'Ligado'
                print('\nRobo ligado\n')
            else:
                self.estado = 'Desligado'
                print('\nRobo desligado\n')

    def movimento(self, lado_andar_robo):
        if self.bateria == 0:
            print('\nBateria zerada, carregue o R2D2')
        else:
            if self.estado == 'Desligado':
                print('\nRobô desligado, ligue-o para movimentar')
            else:
                self.lado_andar_robo = lado_andar_robo
                self.bateria -= 10
                if self.bateria == 0:   #caso o ultimo movimento acabe com a bateria ele desliga na hora, impedindo mais uma
                    self.estado = 'Desligado'   #movimentação

    def controle_energia(self):
        print(f'\n{self.estado}')
        print(self.bateria)

print('_______________Menu_______________')

try:
    bateria = -1
    while bateria > 100 or bateria < 0: #tratamento de erro para forçar o usuário a digitar um valor entre 0 e 100
        bateria = int(input('Digite o nível de bateria do Robo entre 0 e 100%: '))
    R2D2 = Robo(bateria)    #criei um objeto utilizando a variável bateria informada pelo usuário
except ValueError:
    print('Opção inválida!')
else:
    finalizar = ''
    while finalizar != 'sair':
        try:    #aqui é para garantir que seja um número, caso contrário dará erro
            opcao = int(input('\nDigite o número ao respectivo comando que deseja:\n'
                              '1 - Ligar/Desligar o robo\n'
                              '2 - Movimentar o robo\n'
                              '3 - Controle de energia do robô\n'
                              '4 - Finalizar o programa\n'
                              'Escolha: '))
        except ValueError:
            print('Opção inválida!')
        else:
            if opcao == 1:
                R2D2.liga_desliga()
            elif opcao == 2:
                R2D2.movimento(input('Digite o lado para o qual o robô irá andar: '))
            elif opcao == 3:
                R2D2.controle_energia()
            elif opcao == 4:
                finalizar = 'sair'
            else:
                print('\nDigite um número de 1 a 4\n')
finally:
    print('programa finalizado')

#_______________________________________________________________________________________________________________________

3- Crie duas classes (uma para um personagem no video game e outra para o controle do console). O controle deve ser capaz
de fazer o personagem pular, abaixar, desviar para a esquerda e para a direita, sendo comandado, respectivamente pelas
letras W,S,A e D. Use a dica e a função choice() para determinar por onde virá o obstáculo ('cima', 'baixo', 'esquerda'
ou 'direita'), e o tempo para o próximo obstáculo, que deve decair com o aumento de pontos. Cada obstáculo passado gera
+1 ponto. Ainda, crie um loop infinito do jogo até a pessoa perder. Por fim, apresente a pontuação final.
DICA: import time
time.sleep(3) #O programa 'para' por 3 segundos.


"""

class Personagem:

    def __pular(self):
        print('PULOU')

    def apertou_w(self, personagem):
        personagem.__pular()

    def __abaixar(self):
        print('ABAIXOU')

    def apertou_s(self, personagem):
        personagem.__abaixar()

    def __desviar_esquerda(self):
        print('DESVIOU PARA A ESQUERDA')

    def apertou_a(self, personagem):
        personagem.__desviar_esquerda()

    def __desviar_direita(self):
        print('DESVIOU PARA A ESQUERDA')

    def apertou_d(self, personagem):
        personagem.__desviar_direita()

class Controle:

    def controle_w(self, personagem):
        personagem.apertou_w(personagem)

    def controle_s(self, personagem):
        personagem.apertou_s(personagem)

    def controle_a(self, personagem):
        personagem.apertou_a(personagem)

    def controle_d(self, personagem):
        personagem.apertou_d(personagem)

#agora vamos montar a parte principal do jogo, sua lógica geral
import time
from random import choice as ch

vivo = True #irá verificar se o personagem continua vivo ou não durante o jogo
obstaculos = ['CIMA', 'BAIXO', 'ESQUERDA', 'DIREITA']

pontos = -1
tempo = 2

teclado = Controle()
Bob = Personagem()

while vivo:
    passou = False
    pontos +=1
    time.sleep(tempo - pontos/10)
    print('\n')
    obstaculo = ch(obstaculos)
    print(f'Obstáculo: {obstaculo}')
    comando = input('Comando: ')
    if comando == 'w' and obstaculo == 'BAIXO':
        teclado.controle_w(Bob)
        passou = True
    elif comando == 's' and obstaculo == 'CIMA':
        teclado.controle_s(Bob)
        passou = True
    elif comando == 'a' and obstaculo == 'DIREITA':
        teclado.controle_a(Bob)
        passou = True
    elif comando == 'd' and obstaculo == 'ESQUERDA':
        teclado.controle_d(Bob)
        passou = True
    else:
        vivo = False

print('\n')
print('_________________GAME OVER_________________')
print('Obrigado por jogar')
print(f'Pontuação: {pontos} pontos')