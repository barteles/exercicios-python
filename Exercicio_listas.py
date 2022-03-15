""""""
"""
EXERCÍCIO SOBRE LISTAS:
1- Crie duas listas, uma para o carrinho do supermercado que irá receber os produtos comprados e outra
que irá receber os preços dos produtos. Utilizando um loop, preencha as listas com 5 produtos e 5 preços, 
recebendo esses dados do usuário. Por fim, some os preços, imprima o valor total e os intens comprados.

RESULTADO:
carrinho = []    #lista do carrinho
listaPreco = []  #lista de preços dos produtos
valorTotal = 0   #variável que retornará o preço total
count = 0        #variável de parada do loop
produto = ''

while count <5:
    produto = input('Digite o produto: ')
    carrinho.append(produto)    #aqui eu adciono o elemento informado pelo usuário na lista
    preco = float(input('Digite o preço: '))    #aqui adiciono o preço informado na lista
    listaPreco.append(preco)
    count += 1

for id in range(0,5):
    valorTotal += listaPreco[id]    #aqui eu vou somando o valor de cada entrada na variável valorTotal
    #através dos indices, ou seja, valorTotal= listaPreco[0]+ listaPreco[1]+ ... + listaPreco[4]
print(f'O valor total é de R$ {valorTotal}')
print(f'Os produtos comprados foram: {carrinho}')

#__________________________________________________________________________________________________________

2 - Criar um programa de comando de uma loja de jogos. O programa deve conter pelo menos 6 listas: uma indicando
quais os jogos disponíveis, uma indicando o preço de venda do jogo, uma para mostrar a quantidade de jogos disponíveis
na loja para venda, uma informando o preço de fábrica para aumentar os estoques, uma para registrar as vendas e uma para
registrar compras de estoque. Todas as informações de um jogo devem estar no mesmo índice nas listas. Criar um menu 
interativo com as seguintes opções para o usuário: Registrar venda, comprar estoque, Resumo da Loja, Sair. Ao sair, indicar
que o caixa está fechado. O usuário deve controlar o sistema da loja, registrando vendas e as compras de estoque,
sem esquecer de alterar os valores da lista de quantidade.

"""

jogos = ['Gow', 'Minecraft', 'GTA', 'Sonic', 'FIFA']
precoVenda = [ 210.0, 2.99, 150.00, 1.80, 125.00]
