from random import choice as ch

def sorteio(cartela1,cartela2,max):
    numSorteado = []
    numerosIniais1 = []
    numerosIniais2 = []
    vencedor = ''
    sorteador = list(range(1, max + 1))
    while vencedor == '':
        numS = ch(sorteador)    #escolhe um número da lista de números disponíveis
        sorteador.pop(sorteador.index(numS))    #o número escolhido é removido da lista para não haver repetições
        numSorteado.append(numS)
        if numS in cartela1:
            numerosIniais1.append(cartela1.pop(cartela1.index(numS)))   #Se a cartela (lista) da pessoa dispor desse número
#sorteado, ele é removido dela. Em seguida, é adicionado à lista 'numerosIniciais1' para no final, todos os números dessa lista
#serem apresentados como os números que haviam na cartela (lista).
            if len(cartela1) == 0:
                vencedor = 'Joao'
                print(f'Vencedor: {vencedor}')
                print(f'Cartela: {numerosIniais1}')

        if numS in cartela2:
            numerosIniais2.append(cartela2.pop(cartela2.index(numS)))
            if len(cartela2) == 0:
                vencedor = 'Maria'
                print(f'Vencedor: {vencedor}')
                print(f'Cartela: {numerosIniais2}')
    print(f'Números sorteados: {numSorteado}')
