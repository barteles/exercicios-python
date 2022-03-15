""""""
"""
EXERCÍCIO DE NESTED FUNCTIONS:
1- Crie uma função que contenha 3 funções dentro:
 - Uma delas deixa a string toda maíuscula.
 - Outra que soma dois números passados pelo usuário.
 - A ultima soma um número passado pelo usuário com um numero aleatório entre 0 e 15 com o comando randint()
A função mais externa recebe todos os parâmetros com *args e deve fazer tratamentos com try, except caso o usuário passe
de forma errada os dados desejados. A função com args deve receber primeiro o nome da funçao interna que deseja acessar
e os parâmetros necessários nessa ordem especificamente. Ex: funca0_externa('soma_num',2,3), no caso está chamando a função
interna que soma dois números (2,3). Cada função deve imprimir seu resultado.

RESULTADO:
from random import randint

def funcao_externa(*args):
    if args[0] == 'upper_str':
        def upper_str():
            try:
                print(args[1].upper())
            except AttributeError:
                print('Não tem como aplicar .upper() em variáveis que não sejam str')
        return upper_str
    elif args[0] == 'soma':
        def soma():
            try:
                print(f'Soma: {args[1] + args[2]}')
            except TypeError:
                print('Não tem como aplicar soma com variável diferente do tipo float ou int')
        return soma
    elif args[0] == 'soma_ale':
        def soma_ale():
            try:
                print(f'Soma: {args[1] + randint(0,15)}')
            except TypeError:
                print('O parâmetro informado deve ser do tipo int ou float')
        return soma_ale
    else:
        def erro():
            print('Nenhuma função foi chamada!')
        return erro

resposta = funcao_externa('soma_ale', 12.45)
resposta()

resposta = funcao_externa('soma', 12.45, 22)
resposta()

resposta = funcao_externa('upper_str', 'josé bonifácil')
resposta()

resposta = funcao_externa('oi', 'josé bonifácil')
resposta()

#__________________________________________________________________________________________________________

EXERCÍCIO DE DECORADORES:
2- Faça uma função que calcule a diferença entre dois números, decore-a com outra função a partir das mensagens:
'Inicio do programa' e 'Decorando a função'. Após isso, faça com que o decorador permita apenas que seja calculada a 
diferença positiva entre os dois números, independente da ordem de entrada. Imprima o resultado.

RESULTADO::
def decorador(funcao):  #definindo a função decoradora
    def decora(x,y):
        print('__________Inicio do Programa__________')
        print('__________Decorando a função__________')
        if x > y:       #aqui é para testar e garantir que sempre será um número positivo
            funcao(x,y)
        else:
            funcao(y,x) #inverto a posicao dos parâmetros caso o segundo seja maior que o primeiro
    return decora

@decorador
def diferenca(num1, num2):
    print(f'O resultado desejado é: {num1 - num2}')

diferenca(7,1)
diferenca(1,7)

#__________________________________________________________________________________________________________

EXERCÍCIO DE SEÇÃO:
3- Decorar o exercício anterior de Nested Functions e executar as três funções:
 - Na função que executa a string maíuscula use um decorador para imprimir: 'Estou gritando!'
 - Na função que soma os números decore com 'O maior número entre os dois é: {maior}'
 - Na função que soma um número com outro aleatório decore com 'Somando com o número aleatório:'.

"""

from random import randint
from functools import wraps

def decorando_funcoes(funcao):
    @wraps(funcao)  #tratando conservação de metadados com wraps
    def interna(*args,**kwargs):
        if args[0] == 'upper_str':
            print('Estou Gritando!')
        elif args[0] == 'soma':
            if args[1] > args[2]:
                print(f'O maior número é: {args[1]}')
            else:
                print(f'O maior número é: {args[2]}')
        elif args[0] == 'soma_ale':
            print('Somando com aleatório')
        return funcao(*args,**kwargs)
    return interna



@decorando_funcoes
def funcao_externa(*args):
    if args[0] == 'upper_str':
        def upper_str():
            try:
                print(args[1].upper())
            except AttributeError:
                print('Não tem como aplicar .upper() em variáveis que não sejam str')
        return upper_str
    elif args[0] == 'soma':
        def soma():
            try:
                print(f'Soma: {args[1] + args[2]}')
            except TypeError:
                print('Não tem como aplicar soma com variável diferente do tipo float ou int')
        return soma
    elif args[0] == 'soma_ale':
        def soma_ale():
            try:
                print(f'Soma: {args[1] + randint(0,15)}')
            except TypeError:
                print('O parâmetro informado deve ser do tipo int ou float')
        return soma_ale
    else:
        def erro():
            print('Nenhuma função foi chamada!')
        return erro

resposta = funcao_externa('soma_ale', 12.45)
resposta()

resposta = funcao_externa('soma', 12.45, 22)
resposta()

resposta = funcao_externa('upper_str', 'josé bonifácil')
resposta()

resposta = funcao_externa('oi', 'josé bonifácil')
resposta()