""""""
"""
EXERCÍCIOS DE DICIONÁRIO:
1- Faça um programa que contabiliza time de heróis e vilões da seguinte forma:
- Crie um dicionário chamado herói com chave sendo o nome do personagem e elemento o seu poder de 1 a 100.
Ex.: {'Flash':85}
- Crie um dicionário chamado arma com chave sendo a arma e elemento o nível de poder de 1 a 100. 
Ex.: {'Escudo do capitão américa': 60}
- Crie um dicionário chamado vilões com a chave sendo o nome do vilão e o elemento o seu nível de poder de 0 a 200.
Ex.: {'Thanos': 175}
Após isso, o usuário poderá escolher um herói e uma arma que irá combater o vilão, isso irá somar os pontos da arma
e herói e o programa deverá retornar o vencedor, caso seja o herói deverá imprimir a arma usada. Em caso de empate
informe na saída.

RESULTADO:
heroi = {'Flash':90,'Superman':100,'Batman':70,'Capitão América':60,'Hulk':95}
arma = {'Escudo do Capitão América':60,'Arma de gelo':70,'Manopla do infinito':100,'Roupa do pantera negra':80}
vilao = {'Thanos':175,'Darkseider':180,'Coringa':120,'General Zod':140}

heroi_escolha = input('Digite o herói: ')
arma_escolha = input('Digite a arma a ser usada: ')
vilao_escolha = input('Digite o vilão a ser enfrentado: ')

soma_arma_heroi = heroi[heroi_escolha] + arma[arma_escolha]
#encontrando o resultado da luta:
if soma_arma_heroi > vilao[vilao_escolha]:
    print(f'Herói: {heroi_escolha}, com a arma: {arma_escolha}, derrotou {vilao_escolha}:{vilao.get(vilao_escolha)}')
    print(f'Poder do herói: {soma_arma_heroi}')
elif soma_arma_heroi == vilao[vilao_escolha]:
    print(f'Houve um empate')
else:
    print(f'O vilão {vilao_escolha} venceu')
    
 #__________________________________________________________________________________________________________
    
2- Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente em cima da hora. Ele resolveu comprar um
tipo de flor, um presente e escolher um lugar para sairem, anotando as opções abaixo:
        Flores
    tipo            Preço
Rosas vermelhas     145.00
Girassóis           125.00
Margaridas          120.00
Flores do Campo     140.00
        
        Presente
    Tipo            Preço
Urso de Pelúcia     55.00
Caixa de bombom     60.00
Colar               75.00
Roupas              40.00

        Lugar
    Tipo            Preço
Praia               70.00
Sair para jantar    150.00
Parque de diversões 120.00
Hotel               180.00
- Crie um programa que descubra qual a combinação mais cara, em seguida a mais barata e a opção intermediária. Imprima
a combinação em cada caso.

RESULTADO:
flores = {'Rosas vermelhas':145,'Girassóis':125,'Margaridas':120,'Flores do Campo':140}
presentes = {'Urso de pelúcia':55,'Caixa de bombom':60,'Colar':75,'Roupas':40}
lugares = {'Praia':70,'Sair para jantar':150,'Parque de diversões':120,'Hotel':180}

valor_Total = 0 #minha variável que somará os custos para apresentar o maior e menor valor
valor_atual = 0 #variável que serve para receber valores e comparar com o maior e menor valor de 'valor_Total'
flor_escolhida = ''
presente_escolhido = ''
lugar_escolhido = ''
aux = 0

for flor,preco in flores.items():           #os 3 for servem para comparar todas as combinações possíves
    for presente,custo in presentes.items():    #o valor atual irá receber um valor X e irá comparar com o valor_Total
        for lugar,valor in lugares.items():     #e enquanto esse for maior que o Total, será feito o loop.
            valor_atual = preco + custo + valor #quando Total for > atual ele irá terminar o loop e printar as escolhas.
            if valor_Total < valor_atual:
                valor_Total = valor_atual
                flor_escolhida = flor
                presente_escolhido= presente
                lugar_escolhido = lugar
print(f'Maior custo: {valor_Total}, flor:{flor_escolhida}, presente:{presente_escolhido}, lugar:{lugar_escolhido}')

#agora irei criar a lógica para o menor, aqui será uma nova variável auxiliar para o loop dar certo
for flor,preco in flores.items():
    for presente,custo in presentes.items():
        for lugar,valor in lugares.items():
            if aux == 0:
                aux += 1
                valor_Total = preco + custo + valor
            if aux == 1:
                valor_atual = preco + custo + valor
                if valor_Total > valor_atual:
                    valor_Total = valor_atual
                    flor_escolhida = flor
                    presente_escolhido= presente
                    lugar_escolhido = lugar
print(f'Menor valor: {valor_Total}, flor:{flor_escolhida}, presente:{presente_escolhido}, lugar:{lugar_escolhido}')

#para encontrar o valor intermediário, deveria sortear o dicionário do menor para o maior e dividir seu conteúdo
#por 2 e pegar o resultado inteiro, assim pegarei o valor do meio de cada dicionário e farei a soma.
valor_Total = 0
list = []

for flor,preco in flores.items():
    for presente,custo in presentes.items():
        for lugar,valor in lugares.items():
            list.append(valor + custo + preco) #adiciona a soma de cada combinaçao na lista.
list.sort()     #organiza do menor ao maior
valor_Total = list[len(list) // 2]    #pegar o valor do elemento central da lista e armazena no valor_total
                #[len(list) // 2] trará o indice do meio (intermediário da lista).

for flor,preco in flores.items():
    for presente,custo in presentes.items():
        for lugar,valor in lugares.items():
            if valor + preco + custo == valor_Total:    #imprime o custo e a combinação dos valores intermediários
                print(
                    f'Valor intermediário: {valor_Total}, flor:{flor_escolhida},'
                    f' presente:{presente_escolhido}, lugar:{lugar_escolhido}')
                    
#__________________________________________________________________________________________________________

EXERCÍCIO DICT COMPREHENSION:
3- Para todos os números de 1 a 99, use Dict COmprehension para encontrar o digito único mais alto em que qualquer
um dos números é divisível. Ex.: 64 tem o maior divisor de digito único 8, pois 9 não é divisor de 64.

RESULTADO:
#primeiro irei criar uma abordagem para entender como deve ser feito no dict comprehension
resultado = {}

for number in range(1,100):
    lista = []
    for divisor in range(1,10):
        if number % divisor ==0:
            lista.append(divisor)
    resultado[number] = max(lista)
print(resultado)

#dict comprehension;
resultado = {number: max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,100)}
print(resultado)

"""
notaFabio ={5,6,7}
notaClara = {6,7,8}
print(notaClara | notaFabio)