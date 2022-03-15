""""""
import math

"""
EXERCÍCIOS;
1-Faça um programa que peça uma nota (entre 0 e 10). MOstre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.

RESULTADO:
n = float(input('Digite um valor entre 0 e 10: '))
while (n < 0) or (n > 10):
    print('\nValor inválido\n')
    n = float(input('Digite novamente um valor entre 0 e 10: '))
print('\nValor válido')
       
#__________________________________________________________________________________________________________
        
2- Faça um programa que leia um nome de usuário e a senha e não aceite senha igual ao nome do usuário,
mostrando uma mensagem de error e voltando a pedir as informações.

RESPOSTA:
print('_______Bem-Vindo(a)_______')
print('_______Crie um usuário e senha_______')
user = input('Crie o nome do usuário: ')
senha = input('Crie a senha: ')

print('\n_______Cadastro_______')
while user == senha:
    print('\nSenha inválida, escolha uma senha diferente do nome do usuário\n')
    senha = input('Crie a senha: ')
print('\nCadastro confirmado, bem-vindo(a)')

#__________________________________________________________________________________________________________
        
3- Faça um programa que leia e valide as seguintes informações:
    a) NOme: maior que 3 caracteres
    b) Idade: entre 0 e 150 anos
    c) Salário: maior que zero
    d) Sexo: 'f' ou 'm'
    e) Estado civil: 's', 'C', 'V', 'D'
Use a função len(string) para saber o tamanho de um texto

RESULTADO:
nome = input('Digite o seu nome [minimo 4 caracteres]: ')
idade = int(input('Digite a sua idade (entre 0 e 150 anos): '))
salario = float(input('Digite o seu salário [deve  ser maior que $0.00]: '))
sexo = input('Digite o seu sexo: \nf-mulher\nm-homem\nOpção: ')
est_civil = input('Digite o seu estado civil:\ns-solteiro\nc-casado\nv-viúvo\nd-divorciado\nOpção: ')

while len(nome) <=3:
    print('\nNome inválido\n')
    nome = input('Digite o seu nome [minimo 4 caracteres]: ')
while (idade < 0) and (idade > 150):
    print('\nIdade inválida. Digite uma idade entre 0 e 150 anos')
    idade = int(input('Digite a sua idade (entre 0 e 150 anos): '))
while salario < 0:
    print('\nSalário inválido, ele deve ser maior do que zero!')
    salario = float(input('Digite o seu salário [deve  ser maior que $0.00]: '))
while (sexo != 'f') and (sexo != 'm'):
    print('\nDigite novamente o seu sexo!')
    sexo = input('Digite o seu sexo: \nf-mulher\nm-homem\nOpção: ')
while (est_civil != 's') or (est_civil != 'c') or (est_civil != 'v') or (est_civil != 'd'):
    print('\nDigite novamente o seu estado civil!')
    est_civil = input('Digite o seu estado civil:\ns-solteiro\nc-casado\nv-viúvo\nd-divorciado\nOpção: ')
    break

#__________________________________________________________________________________________________________
    
4- Supondo que a população de um país A seja da ordem de 80.000 hab e com taxa de crescimento anual de 3%
e que a população de um país B seja de 200.000 com taxa de crescimento de 1,5%. Faça um programa que calcule
e transcreva o número de anos necessários para que a pop do país A ultrapasse ou igual a do país B, mantidas
as taxas de crescimento.

RESULTADO:
popA = 80000
popB = 200000
anos = 0

while popA <= popB:
    popA = popA * 1.03
    popB = popB * 1.015
    anos += 1
    print(f'Pais A= {popA} e Pais B= {popB}')
print(f'O país A ultrapassará o país B em {anos} anos)

#__________________________________________________________________________________________________________

5- Pegando o exercício anterior, altere o programa e faça com que o usuário dê a população do país A, país B
e suas respectivas taxas de crescimento. Obs.: para que A ultrapasse B, a taxa de crescimento de A deve ser 
maior do que a taxa de crescimento de B.

RESULTADO:
popA = int(input('Digite a população do país A: '))
while popA <0:
    print('\nA população deve ser maior do que 0!')
    popA = int(input('Digite a população do país A: '))
popB = int(input('Digite a população do país B: '))
taxaA = float(input('Digite a taxa de crescimento da pop do país A em % [deve ser maior que 0'
                   'e maior  do que a taxa da pop do país B]: '))
while popB <0:
    print('\nA população deve ser maior do que 0!')
    popB = int(input('Digite a população do país B: '))
taxaB = float(input('Digite a taxa de crescimento da pop do país B em % [deve ser maior que 0'
                   'e menor  do que a taxa da pop do país A]: '))
anos = 0
while popA < popB:
    anos += 1
    popA = int((1+ (taxaA/100)) * popA)
    popB = int((1 + (taxaB / 100)) * popB)
    print(f'\nAno: {anos}')
    print(f'População A= {popA} habitantes')
    print(f'População B= {popB} habitantes')
print(f'\nUltrapassará no ano: {anos}')

#__________________________________________________________________________________________________________

6- Faça um programa que imprima os números de 1 a 20, um abaixo do outro e depois o modifique para aparecer
um ao lado do outro.

RESULTADO:
for num in range(1,21): #aqui o print aparece abaixo um do outro
    print(num)
for num2 in range(1,21):    #aqui o print aparece um ao lado do outro
    print(num2, end= ' ')

#__________________________________________________________________________________________________________
    
7- faça um programa que leia 5 números e retorne o maior entre eles
8- Pegando o mesmo programa anterior, faça com que mostre também a soma e a média.

RESULTADO:
numeros = int(input('Quantos números: '))
primeiro = int(input('Numero 1:'))

count = 1
maior = primeiro
soma = primeiro

while count < numeros:
    count += 1
    temp = int(input(f'Digite o numero {count}: '))
    soma += temp
    if temp > maior:
        maior = temp
media = soma / numeros
print(f'A soma é: {soma}')
print(f'A média é: {media}')
print(f'O maior número é: {maior}')

#__________________________________________________________________________________________________________

9- Faça um programa que imprima na tela apenas os números impares de 1 a 50.

RESULTADO:
number = 0              #criei a variável com valor inicial 0
while number <= 49:     # o loop vai realimentar ela e assim gerar valores impares até 50
    number = number + 1 
    if number % 2 != 0: #se resto de number for diferente de 0, faça:
        print(f' {number} é impar') #imprima que o número é impar.
        
#__________________________________________________________________________________________________________

10- Faça um programa que receba dois números inteiros e gere os números inteiros que 
estao no intervalo entre eles.

RESULTADO:
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

while n1 < (n2 - 1):
    n1 += 1
    print(n1)

#__________________________________________________________________________________________________________

11- Altere o programa anterior para mostrar a soma final entre eles

RESULTADO:
lista = []
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
for i in range(n1 + 1, n2):
    lista.append(i)     #não sei a função append
    print(i)
print(f'Soma do intervalo = {sum(lista)}').

#__________________________________________________________________________________________________________

12- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O
usuário deve informar de qual número ele deseja ver a tabuada.

RESULTADO: 
n1 = int(input('Digite o número da tabuada: '))
n2 = 1
while n2 < 11:      #fiz com que n2 varie entre 1 e 10, assim gerando toda a tabuada.
    print(f'{n1} x {n2} = {n1 * n2}')
    n2 +=1

#__________________________________________________________________________________________________________    

13- Faça um programa que peça 2 números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo numero. Nao utiliza a função de potência da linguagem.

RESULTADO:
n1 = int(input('Digite a base: '))
n2 = int(input('Digite o expoente: '))
print(f'{n1} ^ {n2} = {n1 ** n2}')   # o sinal de ** é o sinal usado para expoente

#__________________________________________________________________________________________________________

14- Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números ímpares.

RESULTADO:
par = 0         #minha variável que conta os pares
impar = 0       #minha variável que conta os impares
count  = 0      #minha variável de parada do loop
while count < 10:
    n1 = int(input(f'Digite o {count + 1}º número inteiro: '))      #assim o usuário preenche os 10 numeros inteiros
    if (n1 % 2) == 0:                       #se o número dividido por 2 for resto 0, ele conta como par 
        par += 1                            #aqui incrementa em 1 o número de paress
        count += 1                          #se satisfeito, incrementa o count em 1 (contando como par)
    else:
        count +=1                           #se não satisfeito, incrementa o count em 1 (contando como impar)
        impar += 1
print(f'O número de pares é: {par}\n o número de impares é: {impar}')

#__________________________________________________________________________________________________________

15- A série de Fibonacci é formada pela sequência: 1,1,2,3,5,8,13,21,34,55,... Faça um programa que 
gere a série até o n-ésimo termo.

RESULTADO:
anterior = 0    
proximo = 1     #a sequência de fibonacci sempre inicia em 1.
parada = int(input('Digite o n-ésimo termo: '))     #inserir quantos termos devem ter na sequência
count = 0       #minha variável que vai dar o break
while count < parada:
    print(proximo)                  #imprimir o número antes de ele se auto alimentar
    proximo = proximo + anterior    #aqui ele irá se alimentar usando o próximo(anterior) e o anterior(anterior)
    anterior = proximo - anterior   #gerando assim os números seguintes na sequência
    count += 1

#__________________________________________________________________________________________________________

16 -A série de Fibonacci é formada pela sequência: 1,1,2,3,5,8,13,21,34,55,... Faça um programa que 
gere a série até que o valor seja maior que 500.

RESULTADO:
anterior = 0
proximo = 1
count = 0
while count < 15:       #o 15° termo é maior que 500
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    count += 1

#__________________________________________________________________________________________________________    

17- Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5! = 5*4*3*2*1= 120

RESULTADO:
numero = int(input('Digite o fatorial: '))
resultado = 1
for n in range(numero, 0, -1):
    print(f' {n} * ')
    resultado = resultado * n
print(resultado)

#__________________________________________________________________________________________________________

18- Faça um programa que dado um conjunto de N números, determine o menor valor, o maior valor
e a soma dos valores.

????

19- Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

????

20- Altere o programa do cálculo fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
limitando o fatorial a numeros inteiros positivos e menores que 16.

RESULTADO:
while input('Deseja continuar? s- sim, n- não\nOpção: ') == 's':        #aqui criei um loop para continuar enquanto
                                                                        #o usuário quiser
    numero = int(input('Digite o fatorial positivo e menor que 16: '))
    resultado = 1
    if numero > 0 and numero < 16:          #caso a condicional funcione, ele fará o fatorial
        for n in range(numero, 0, -1):
            print(f' {n} * ', end=' ')
            resultado = resultado * n

    else:                                   #caso falhe, trará que o valor é invalido
        print('Valor inválido, tente novamente')
    print(f'= {resultado}')
"""




while input('Deseja continuar? s- sim, n- não\nOpção: ') == 's':        #aqui criei um loop para continuar enquanto
                                                                        #o usuário quiser
    numero = int(input('Digite o fatorial positivo e menor que 16: '))
    resultado = 1
    if numero > 0 and numero < 16:          #caso a condicional funcione, ele fará o fatorial
        for n in range(numero, 0, -1):
            print(f' {n} * ', end=' ')
            resultado = resultado * n

    else:                                   #caso falhe, trará que o valor é invalido
        print('Valor inválido, tente novamente')
    print(f'= {resultado}')



