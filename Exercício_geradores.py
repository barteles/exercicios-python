""""""
"""
EXERCICIO GERADORES:
1- Crie uma lista que armazene inteiros de um usuário em um loop até que o usuário não deseje mais adicionar, trate o erro
com try/except caso o usuário digite uma letra ao invés de um número. Passe essa lista para uma função geradora que reconhecerá
quais são os números primos dentro da lista passada inicialmente. Caso seja um número primo, retorne pelo método yield, caso 
contrário passa para o próximo número. Ao final, imprima os valores retornados pelo yield em forma de tupla

"""
def num_primos(listaNum):       #para numeros primos
    for item in listaNum:
        divisor = 1             #meu divisor deve ser diferente de 0
        num_divisor = 0         #o número de divisores que cada item terá
        while divisor <= item:  #cada numero posto será dividido pelo divisor +1, ou seja, num =11 >> 11/1, 11/2, 11/3
            # e assim por diante e quando esse divisor tiver resto 0, irá alimentar o num_divisor
            if item % divisor == 0:
                num_divisor +=1
                divisor +=1
            else:
                divisor +=1
        if num_divisor ==2:     #números primos são dividos somente por 1 e eles mesmos, por isso num_divisor = 2
            yield item


listaNum = []
sair = ''
while sair != 'sim':
    try:
        num = int(input('Digite um número: '))
        listaNum.append(num)
    except ValueError:
        print('Digite somente números')
    else:
        sair = input('Deseja parar? (sim - não): ')

tuple_primos = tuple(num_primos(listaNum))
print(f'Tupla contendo todos os primos: {tuple_primos}')

