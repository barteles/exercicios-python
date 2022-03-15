"""
EXERCÍCIO DE ARGS E KWARGS
1- Faça um sistema de uma corrida entre Mercúrio, Papa-leguas, Sonic, Flash, Ligeirinho e Super-homem (MC,PL,SN,FL,LG,SH).
Crie uma função que receba os 6 corredores em ordem de vencedor até o útilmo (pedir ao usuário), sendo as três primeiras
variáveis obrigatórias e as 3 ultimas em kwargs, com as chaves sendo as posições na corrida. Pedir ao usuário se houve
trapaça:
 - se não houve: apresentar a classificaçao final.
 - se houve: pedir ao usuário quem trapaceou e quem foi prejudicado. Depois trocalos de posições. Por fim, apresentar
 a classificação final.

RESULTADO:
def classParcial(primeiro, segundo, terceiro, **outros):
    op = input('Houve trapaça? s/n: ')
    quarto = ''
    quinta = ''
    ultimo = ''
    if op == 'n':
        for posicao, corredor in outros.items():
            if posicao == '4':
                quarto = corredor
            elif posicao == '5':
                quinto = corredor
            elif posicao == '6':
                ultimo = corredor
        classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo)

    elif op == 's':
        colocacao = [primeiro, segundo, terceiro]
        colocacao.extend(outros.values())   #adiciona à lista os valores do dicionário

        babaca = input('Quem trapaceou? : ')
        vitima = input('Quem foi trapaceado? : ')

        posBabaca = colocacao.index(babaca)
        posVitima = colocacao.index(vitima)

        colocacao[posBabaca] = vitima
        colocacao[posVitima] = babaca

        classFinal(*colocacao)

    else:
        print('Digite uma opção válida: ')

def classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo):
    print('Classificação Final:')
    print(f'Primeiro: {primeiro}')
    print(f'Segundo: {segundo}')
    print(f'Terceiro: {terceiro}')
    print(f'Quarto: {quarto}')
    print(f'Quinto: {quinto}')
    print(f'Ultimo: {ultimo}')



print('Corredores:')
print('Mercúrio (MC), Papa-léguas (PL), Sonic (SN), Flash (FL), Ligeirinho (LG) e Super-Homem (SH)')

prim = input('Vencedor: ')
seg = input('Segundo: ')
terc = input('Terceiro: ')
qua = input('Quarto: ')
qui = input('Quinto: ')
ult = input('Ultimo: ')

outros = {'4':qua,'5':qui,'6':ult}  #gera um dicionário (kwarg) com os três ultimos da corrida

classParcial(prim, seg, terc, **outros)

"""

"""
EXERCÍCIO DE SEÇÃO:
1- Faça uma funçao que receba um número inteiro maior que zero e retorne a soma de todos os algarismos.
Caso o valor seja negativo retorne 'Numero inválido'
Exemplo: 251 = 2+5+1 =8.

RESULTADO:

def soma_algarismo(numero): #para quebrar um número em algarismos, deve-se fazer o seguinte:
    divisor = 1     #variável que descobre quantos algarismos terei
    num_algarismo = 0   #variável que conta o número de algarismos
    while True:
        if (numero // divisor) == 0:    #25 // 1 = 25; 25 // 2= 2; 25 // 3=0
            break
        else:
            num_algarismo += 1
            divisor *= 10
    soma = 0
    for valor in range(num_algarismo):  
        soma += ((numero// (10 ** valor)) % 10) #atualiza a soma de acordo com:
        #Exemplo: 251
        #251 = 2 * 10^2 + 5 *10^1 + 1 * 10^0
        #251 // 100 = 2
        #251 // 10 = 25 % 10 = 5  (25/ 10 = 2, sobra 5)
        #251 // 1 = 251 % 10 = 1  (251/10 = 25, sobra 1)
        #assim:
        #(251 // (10 ** 0) % 10) = 1
        # (251 // (10 ** 1) % 10) = 5
        # (251 // (10 ** 2) % 10) = 2
        # (251 // (10 ** 3) % 10) = 0
    return soma

numero = int(input('Digite um número: '))
if numero >= 0:
    print(soma_algarismo(numero))
else:
    print('Valor inválido')
"""

