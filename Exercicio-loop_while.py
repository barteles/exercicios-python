""""""
"""
Exercício loop while
1- Faça um programa que calcule o maior palindromo resultado do produto de dois números
de 3 dígitos.
Ex.: o maior palídromo do produto de 2 números de 2 digitos é: 91*99= 9.009

RESULTADO:
n1 = 999    #inicia o primeiro número
res = 0     #inicia o resultado
while n1 != 99:     #enquanto o n1 for diferente de 99, faça:
                    #esse loop faz: 999*n2, 998*n2, ..., 100*n2
    n2 = n1         #inicia o segundo número para fazer n1 * n2
    while n2 != 99:      #Enquanto o seg número for diferente de 99, faça:
                         #esse loop irá de 999,..., 99 (sendo reduzido de 1 em 1)
                         # n1*999, n1*998, ... , n1*100
        numero = str(n1 * n2)         #transforma em string o resultado do produto
        inverte_numero = numero[::-1]   #inverte o produto de n1 e n2
        if inverte_numero == numero:
            num = int(numero)       #aqui eu voltei o número para um inteiro
            if res < num:
                res = num           #armazena o num em res pois num é maior
                n2 -= 1             #reduz n2 em 1
            else:
                n2 -= 1
        else:                       #caso o inverso do número não seja igual ao número, faça:
            n2 -= 1
    n1 -= 1
print(res)

#__________________________________________________________________________________________________________

EXERCÍCIOS SEÇÃO LOOP
1- Faça um programa que calcule a média dos 5 primeiros números primos da sequência de Fibonacci.
Fibonacci: 1,1,2,3,5,8,13,21,34,55,...

#vamos começar fazendo a sequência de Fibonacci
#declarando as primeiras variáveis
anterior = 0
proximo = 1     #Fibonacci deve sempre iniciar em 1.
parada = 1 #essa sera minha variável que vai dar o break do loop

while parada <= 5:
    print(proximo)
    proximo = proximo + anterior    #aqui ele irá incrementar e avançar de casa
    anterior = proximo - anterior   #para que próximo avance de casa, anterior também o deve fazer
    parada = parada + 1

AGORA VAMOS APRENDER A FAZER NÚMEROS PRIMOS
 - Para ser primo, ele deve ser maior que 1 e divisível somente por 1 e por ele mesmo
 
 proximo = proximo + anterior    #aqui ele irá incrementar e avançar de casa
    anterior = proximo - anterior   #para que próximo avance de casa, anterior também o deve fazer
    divisor = 1
    num_divisores = 0
    while divisor <= proximo:
        if proximo % divisor == 0:  #quando o resto da divisão de proximo por divisor for 0, faça:
            num_divisores += 1      #incrementa o num_divisores quando for satisfetia a condiçao
        divisor += 1                #incrementa diretamente o divisor e volta o loop.
    if num_divisores == 2:          #aqui está a condição para ele ser número primo
        soma = soma + proximo       #soma serve somente para encontrar a média
        print(proximo)
        
RESULTADO FINAL:

anterior = 0
proximo = 1     #Fibonacci deve sempre iniciar em 1.
parada = 1      #essa sera minha variável que vai dar o break do loop
soma = 0        #essa variável serve somente para encontrar a média

while parada <= 5:
    proximo = proximo + anterior    #aqui ele irá incrementar e avançar de casa
    anterior = proximo - anterior   #para que próximo avance de casa, anterior também o deve fazer
    divisor = 1
    num_divisores = 0
    while divisor <= proximo:
        if proximo % divisor == 0:  #quando o resto da divisão de proximo por divisor for 0, faça:
            num_divisores += 1      #incrementa o num_divisores quando for satisfetia a condiçao
        divisor += 1                #incrementa diretamente o divisor e volta o loop.
    if num_divisores == 2:          #aqui está a condição para ele ser número primo
        soma = soma + proximo       #soma serve somente para encontrar a média
        print(proximo)
        parada += 1                 #incrementa parada até 5 para então interromper o loop geral.
print(soma/5)
"""


anterior = 0
proximo = 1     #Fibonacci deve sempre iniciar em 1.
parada = 1      #essa sera minha variável que vai dar o break do loop
soma = 0        #essa variável serve somente para encontrar a média

while parada <= 5:
    proximo = proximo + anterior    #aqui ele irá incrementar e avançar de casa
    anterior = proximo - anterior   #para que próximo avance de casa, anterior também o deve fazer
    divisor = 1
    num_divisores = 0
    while divisor <= proximo:
        if proximo % divisor == 0:  #quando o resto da divisão de proximo por divisor for 0, faça:
            num_divisores += 1      #incrementa o num_divisores quando for satisfetia a condiçao
        divisor += 1                #incrementa diretamente o divisor e volta o loop.
    if num_divisores == 2:          #aqui está a condição para ele ser número primo
        soma = soma + proximo       #soma serve somente para encontrar a média
        print(proximo)
        parada += 1                 #incrementa parada até 5 para então interromper o loop geral.
print(soma/5)