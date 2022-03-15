"""
EXERCÍCIO DE FUNÇÕES SEM PARÂMETROS:
1- Foi realizada uma pesquisa de algumas caracteristicas e gostos de quatro habitantes, incluindo: nome, sexo, esporte
favorito (natação, futebol, volêi, tênis) e idade. Com esses dados faça:
- Função que armazene os dados em uma lista. Dica: Use dicionários dentro da lista.
- Calcule a idade média de homens que gostam de natação. Caso não haja homens que gostam de nataçao, chame uma funçao
e imprima o aviso que não há homens que gostam de natação.

RESULTADO:
def cadastro():
    list = []
    for i in range(4):
        dicionario = dict(nome = input('Digite seu nome: '),
                          sexo = input('Digite M para masculino e F para feminino: '),
                          esporte = input('Digite seu esporte favorito entre natação, futebol, volêi e tênis: '),
                          idade = int(input('Digite sua idade: ')))
        list.append(dicionario)
    return list

def aviso():
    print('Não há homens que gostam de natacao')

lista = cadastro()
cont =0
soma = 0

for i in range(4):
    if lista[i]['sexo'] == 'M' and lista[i]['esporte'] == 'natacao':
        soma = soma + lista[i]['idade']
        cont += 1
if cont == 0:
    aviso()
else:
    print(f'idade total: {soma} anos, número de homens: {cont}')

#__________________________________________________________________________________________________________

EXERCÍCIO FUNÇÕES COM PARÂMETROS:
2- Criar uma função recursiva (que retorne ela mesma) para armazenar N termos da sequência de Fibonacci em uma lista.
N é definido pelo usuário. Ao encontrar os termos, imprimir a lista e finalizar a função.

RESULTADO>
listaFib = []
stop = 0

def fibonacci(stop, a, b, aux):
    global listaFib     # Uso esse comando para utilizar uma variável global na minha função
    listaFib.append(a)      #adciona os valores na lista
    a, b = b, a + b     #lógica para a sequência de fibonacci
    aux += 1

    if stop == aux:
        print(listaFib)
        return 0
    else:
        return fibonacci(stop, a, b, aux)   #chama a própria função até que aux == stop

while stop < 1:
    stop = int(input('Digite o número de termos: '))

fibonacci(stop, a = 1, b =1, aux=0)

#__________________________________________________________________________________________________________

3- Criar 5 funções: uma para cadastro, outra para realizar login, outra para mudar senha, outra para realizar logout
e ainda uma para definir qual opção o usuário deseja escolher.
Utilize um loop while para sair do sistema apenas se o usuário desejar (criar a opçao 'sair'). Atente-se as regras:
 - Só é possível realizar um cadastro se não houver anterior.
 - Só é possível realizar login se houver cadastro.
 - Só é possível realizar login se o usuário informar corretamente username e senha.
 - Só é possível alterar senha se o usuário estiver logado.
 - Só é possível alterar senha se o usuário informar corretamente a senha atual.
 - Só é possível realizar logout se o usuário estiver logado.
"""

login = False
cadastroFeito = False
username = ''
senha = ''
op = 0


def intro():
    global op
    global cadastroFeito
    global login
    while op != 5:
        print('1- Cadastro\n2- Login\n3- Mudar Senha\n4- Logout\n5- Sair')
        op = int(input('______Opção: '))

        if op == 1:
            if not cadastroFeito:  # se NÃO existir cadastro feito:
                cadastro()
            else:
                print('\n__________Cadastro feito anteriormente__________\n')

        elif op == 2:
            if cadastroFeito:
                loginSistema()
            else:
                print('\n__________Faça o cadastro primeiro_________\n')

        elif op == 3:
            if cadastroFeito:
                mudarSenha()

            else:
                print('\n_________Faça o cadastro primeiro_________\n')

        elif op == 4:
            if login:
                logout()
            else:
                print('\n_________Usuário precisa estar logado_________\n')

        elif op == 5:
            print('_________Processo finalizado!__________')
            return 0


def cadastro():
    global username
    global senha
    global cadastroFeito

    username = input('\n________Digite o nome do usuário: ')
    senha = input('_________Digite a senha: ')
    cadastroFeito = True
    print('\n_________Cadastro realizado com sucesso!_________\n')
    return intro()


def loginSistema():
    global username
    global senha
    global login
    if not login:
        teste_username = input('_________Username: ')
        teste_senha = input('_________Senha: ')

        if teste_senha == senha and teste_username == username:
            login = True
            print('\n_________Você está logado_________\n')
            return intro()
    if login:
        print('\n_________Você está logado_________\n')
        return intro()
    else:
        print('\n_________Senha ou usuário incorretos_________\n')
        return intro()




def mudarSenha():
    global senha
    global login

    if login:
        teste_senha = input('_________Digite a senha atual: ')
        if teste_senha == senha:
            senha = input('\n_________Digite a nova senha: ')
            print('\n__________Senha alterada com sucesso!_________\n')
        else:
            print('\n_________Senha incorreta_________\n')
    else:
        print('_________Faça o login antes_________')
    return intro()


def logout():
    global login
    login = False
    print('__________Deslogado!__________')
    return intro()


intro()
