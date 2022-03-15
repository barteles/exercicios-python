"""
EXERCÍCIO DE MÓDULOS INTEGRADOS RANDOM:
1- Utilize o módulo random e suas funções pra realizar os procedimentos seguintes:
 a) random() | Obter um numero aleatório inteiro entre 1 e 10 e armazenar em uma variável x.
 b) randint() | Obter x numeros aleatórios inteiros entre 0 e 100 e armazena-los em uma lista.
 c) shuffle() | Embaralhar a lista.
 d) choice () | selecionar um elemento aleatório da lista.
 e) loop | imprimir os números da lista que são maiores que o número selecionado.

"""
from random import (
    random as rd,
    randint as ri,
    shuffle as sh,
    choice as ch
)

x = round(rd() * 10)    #número aleatório (entre 0 e 1) multiplicado por 10 e inteiro (round)
print(x)

lista = []
for i in range(x):
    lista.append(ri(0,100))

print(lista)

sh(lista)   #embaralha a lista
print(lista)

escolhido = ch(lista)
print(f'O número aleatório escolhido foi: {escolhido}\n')

print(f'Números maiores que o escolhido: ', end = ' ')


maiores  = filter(lambda x: x > escolhido, lista)
print(list(maiores), end=' ')