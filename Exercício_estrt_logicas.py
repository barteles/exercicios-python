""""""
"""
Exercício de estruturas lógicas:
1- Crie um sistema de cadastro de login de um site, utilizando um username e senha informados pelo usuário


EXERCÍCIOS DE SEÇÃO:
1-Crie um programa que encontre e imprima as raízes de uma equação do segundo grau, utilizando Bhaskara.
RESPOSTA:


print('-------Bem vindo(a) ao cadastro do site-------')
print('-------Crie um usuário e senha-------')

login = False
user = input('Digite o nome do usuário: ')
senha = input('Digite sua senha: ')

print('\n_________LOGIN_________')
if input('Usuário:') == user and input('Senha') == senha:
    login = True

if login:
    print(f'\nBem-vindo(a) {user}')
else:
    print('\nTente novamente')
    
    
    
#mesma resposta, porém usando o NOT

print('-------Bem vindo(a) ao cadastro do site-------')
print('-------Crie um usuário e senha-------')

login = False
user = input('Digite o nome do usuário: ')
senha = input('Digite sua senha: ')

print('\n_________LOGIN_________')
if input('Usuário: ') == user and input('Senha: ') == senha:
    login = True

if not login:
    print(f'\nTente novamente')
else:
    print(f'\nBem-vindo(a) {user}')
    
    
    
#mesma resposta, porém usando IS

print('-------Bem vindo(a) ao cadastro do site-------')
print('-------Crie um usuário e senha-------')

login = False
user = input('Digite o nome do usuário: ')
senha = input('Digite sua senha: ')

print('\n_________LOGIN_________')
if input('Usuário: ') == user and input('Senha: ') == senha:
    login = True

if login is True:
    print(f'\nBem-vindo(a) {user}')
else:
    print(f'\ntente novamente')
    
    
REPOSTA EXERCÍCIO DE SEÇÃO:
print('-------Crie uma equação de Segundo Grau-------')
print('Do tipo: ax² + bx + c')

a = int(input('Digite o termo ax² da equação: '))
b = int(input('Digite o termo bx da equação: '))
c = int(input('Digite o termo c da equação: '))

delta = (b ** 2) - (4 * a * c)
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print(f'\nResultado: x1= {x1} e x2= {x2}')

#podemos escrever raiz de outra maneira tbm:
x1 = (-b + math.sqrt(delta)) / (2 * a)

"""

print('-------Crie uma equação de Segundo Grau-------')
print('Do tipo: ax² + bx + c')

a = int(input('Digite o termo ax² da equação: '))
b = int(input('Digite o termo bx da equação: '))
c = int(input('Digite o termo c da equação: '))

delta = (b ** 2) - (4 * a * c)
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print(f'\nResultado: x1= {x1} e x2= {x2}')