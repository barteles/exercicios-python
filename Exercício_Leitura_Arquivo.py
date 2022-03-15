
"""
EXERCÍCIO SOBRE LEITOR DE ARQUIVOS:
1- Crie um arquivo de texto na pasta onde está o programa Python. O arquivo deve conter alguns números de 4 digitos
separados por linha, representando números de uma rifa. Após isso, itere o arquivo para colocar os valores em uma lista.
Por fim, utilize a função choice() pra determinar o ganhador

RESULTADO:
from random import choice as ch

numeros_rifa = []
with open('rifa.txt') as rifa:
    for num in rifa:
        numeros_rifa.append(int(num))       #o int é para tirar o \n que vem junto dos números

print(f'O vencedor é: {ch(numeros_rifa)}. Parabéns!')

#__________________________________________________________________________________________________________

2- Crie um arquivo com conteúdo aleatório. Em seguida, abra o arquivo, leia-o 3 vezes a partir dos caracteres 5,9,14.
Por fim, feche o arquivo.

RESULTADO:
arquivo = open('aleatorio.txt')
print(arquivo.read())
print('-'*50)

arquivo.seek(5)
print(arquivo.read())
print('-'*50)
arquivo.seek(9)
print(arquivo.read())
print('-'*50)
arquivo.seek(14)
print(arquivo.read())

arquivo.close()

#__________________________________________________________________________________________________________

3 - Criar um arquivo de texto, inserir o lucro mensal de uma startup entre os meses de janeiro a maio, informando o mês
e o valor, através da entrada de usuário. Após isso, ler o arquivo e imprimir o mês de maior lucro.

RESULTADO:
with open('lucrosEmpresas.txt', 'w') as LE:
    while True:
        mes = input('Mês: ')
        if mes == 'sair':
            break
        else:
            LE.write(f'{mes}: ')
            LE.write(input('Lucro: '))
            LE.write('\n')

relatorio = {}

with open('lucrosEmpresas.txt') as LE:
    for linha in LE:
        relatorio[linha[0:3]] = int(linha[5:])  #a chave do dicionário será o mês (posição 0 a 3), e o valor será o lucro
#(posição 6 em diante, por causa do DOIS PONTOS e do espaço após mês)

print(relatorio)
maiorLucro= 0
mes_Maior_Lucro = ''

for mes,lucro in relatorio.items():
    if lucro > maiorLucro:
        maiorLucro = lucro
        mes_Maior_Lucro = mes

print(f'Mês de maior lucro: {mes_Maior_Lucro} com {maiorLucro} reais')

#__________________________________________________________________________________________________________

4- Teste se um arquivo chamado livros.txt não exista pela abertura X, caso o arquivo já exista abra com o comando W+,
utilize Try/Except nesta manipulação. Imprima na tela qual foi o modo de abertura, escreva no bloco o nome dos 3 melhores
livos que você já leu (um em cada linha) adicionando ao arquivo, feche-o. Abra-o novamente e adicione mais um livro ao final
do arquivo sem apaga-lo, por fim, leia a versao final.

RESULTADO:
try:
    with open('livros.txt', 'x') as arq:    #caso não exista o 'livros.txt', o mesmo será criado, porém se existir
        print("Abrimos no modo 'x'")    #apresentará um error
        arq.write('\nThe Expanse series')
        arq.write('\nOld mans war')
        arq.write('\nAprendiz de de assassino')
except FileExistsError:     #caso já exista, ele irá entrar no except e abrirá pelo 'w+'
    with open('livros.txt', 'w+') as arq:
        print("Abrimos no modo 'w+' ")
        arq.write('\nThe Expanse series')
        arq.write('\nOld mans war')
        arq.write('\nAprendiz de de assassino')

with open('livros.txt', 'a+') as arq:   #aqui basicamente dá um 'append' e adiciona mais informação sem apagar a anterior
    arq.write('\nA roda do tempo')
    arq.seek(0)
    print(arq.read())

#__________________________________________________________________________________________________________

EXERCÍCIO DE SEÇÃO:
5- Faça um programa utilizando um arquivo chamado 'NotasEscola.txt' para gerenciar as notas dos alunos de uma classe.
O main deve conter um menu com as seguintes opções: a)Inserir alunos e notas, b) Exibir os alunos e a média final,
c) Alunos aprovados e reprovados, d) Sair. Produza uma função para cada opção.

"""

def inserir():
    with open('NotasEscola.txt', 'a') as NE:    #aqui será em modo 'a' para dar append nos dados
        NE.write('Aluno(a): '+ input('Aluno(a):') + ' ' + 'Nota: '+ input('Nota: '))
        NE.write('\n')
    print('\nDados inseridos!\n')

def exibir():
    with open('NotasEscola.txt') as NE: #aqui só será aberto o modo leitura para verificar os nomes e dados dos alunos
        print(NE.read())
    print('\nDados apresentados!\n')

def situacao():
    with open('NotasEscola.txt') as NE:
        listaLinhas = NE.readlines()    #aqui será criado uma lista onde cada elemento é uma linha do arquivo lido
        for dado in listaLinhas:
            id1= dado.index(':') #o índice apresentado será o primeiro ':' encontrado
            id2= dado.index('Nota') #aqui ele irá apresentar o índice da letra N de 'Nota'
            nome = dado[id1 + 1: id2 - 1] #id1 + 1 é para retirar o espaço em branco após o ':' e id2 - 1 é para pegar tudo
            #o que estava antes do índice da letra 'N' de 'Nota', ou seja, somente o nome do aluno(a)
            id3 = dado.index(':', 9) #aqui ele irá procurar um ':' A PARTIR do indice 9, portanto ignorando o primeiro ':'
            nota = float(dado[id3 + 1:])
            if nota >= 6:
                print(f'{nome} APROVADO!')
            else:
                print(f'{nome} REPROVADO')
            print('\n')


op = 1

while op != 0:
    print('Menu:\n1- Inserir aluno e nota\n2- Exibir alunos e medias finais\n3- Alunos aprovados e reprovados\n4- Sair')
    op = int(input('Opçao: '))
    print('\n')
    if op == 1:
        inserir()
    elif op == 2:
        exibir()
    elif op ==3:
        situacao()
    else:
        break