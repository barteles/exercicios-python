""""""
"""
Exercícios de Loop
1-Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário. 
Ex: se o user escolheu 10, temos 1+2+5+10 = 18.
2- Faça um programa que imprima os n primeiros multiplos de 5, sendo n definido pelo usuário.
Ex: se o user escolheu n=3, será impresso 5, 10, 15.

RESOLUÇÃO:
1- soma = 0 #Inicializa a variável soma
numero = int(input('Digite o número: ')) #pede o número ao usuário
for num in range(1, numero + 1):  #para cada num dentro do intervalo de 1 a numero+1, faça:
    if numero % num == 0:  #se o resto da divisão por num for zero, faça:
        soma = soma + num  #atualiza a soma com o num
        print(num)

print(soma)  #Imprima a soma final

#__________________________________________________________________________________________________________

2- n = int(input('Digite o número n: '))
for multiplos in range(0, 5 * n + 1,5):
    print(f'Multiplos: {multiplos}')

OU

numer =  int(input('Digite o número: '))
for nu in range(1, numer + 1):
    print(f'{5 * nu}')
"""

