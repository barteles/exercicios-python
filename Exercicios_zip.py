"""
EXERCÍCIO DE ZIP:
1- Está acontecendo uma gincana na escola e você foi escolhido para realizar o controle da pontuação! Para isso, crie 4
listas (a primeira com nome dos participantes e as outras 3, cada uma representandoa  pontuação de uma prova). Armazenar
os valores de 0 a 100, ou seja, as notas que cada participante obteve. Por fim, utilize zip() para retornar um dicionário
com o nome de cada aluno como chave e o somatório de suas notas em cada prova como valor. Após isso, imprima o participante
vencedor.

RESULTADO:
nomes = ('Bianca', 'Giovani', 'Ariel', 'Guilherme', 'Napoleão')
prova1 = (2, 0, 9.5, 8, 6)
prova2= (3, 6, 7.4, 5.3, 2.5)
prova3 = (7.8, 7.5, 9.5, 10, 9)
listaNotas = []

tabela = zip(prova1, prova2, prova3) #agrupa a nota das 3 provas em uma tupla para cada participante
#print(list(tabela))
for notas in tabela:
    listaNotas.append(sum(notas)) #soma as 3 provas de cada participante e adiciona na lista
    #print(listaNotas)
tabelaFinal = zip(nomes,listaNotas) #aqui ele associa o nome às notas

dicioFinal = dict(tabelaFinal)
vencedor = ''
pontos = 0      #variável para receber os pontos do vencedor

for part, pts in dicioFinal.items():
    print(f'Participante: {part}. Pontos: {pts}')
    if pts > pontos:
        pontos = pts
        vencedor = part
print(f'\n______Vencedor: {vencedor} - Pontos: {pontos}')
"""

"""
EXERCÍCIO DE SEÇÃO:
1- Crie 3 listas, uma com o nome de 3 companhias aéreas, e as outras 2 representando o numero de passageiros por companhia
em dois voos: voo1 e voo2. Utilize zip(), lambda e map() para obter o valor máximo de passageiros por companhia nos dois voos
e associar estes valores com os nomes das companhias, formando uma lista de tuplas. Por fim, utilizar Filter() e lambda
para determinar a classificação da companhia, conforme indicado nos dados abaixos:
Dados:
0 < Passageiros <= 100: 1 estrela
100 < Passageiros <= 200: 2 estrelas
200 < Passageiros <= 300: 3 estrelas

RESULTADO:


"""

companhias = ['GOL', 'LATAM', 'AZUL']
voo1 = [115, 95, 110]
voo2 = [105,80,225]

voos1e2 = zip(voo1,voo2)    #aqui eu juntei os valores das listas voo1 e voo2 (de cada companhia/indice)
# em uma única lista de tuplas
#print(list(voos1e2))
maxPass = map(lambda voos: max(voos), voos1e2)  #determina o valor máximo de passageiros por companhia, lembrando que
#map serve para que a função lambda seja executada todas as vezes diretamente para criar uma nova lista como resultado,
# ao invés de ter de adicionar cada valor de uma vez
listaMaxPass = list(maxPass)    #poderia ter adiantado a criaçao de lista no próprio maxPass
#print(listaMaxPass)
compMax = list(zip(companhias, listaMaxPass)) #juntei os valores de máximo de passageiros com as respectivas companhias
#print(compMax)

umaEst = list(filter(lambda valMax: valMax[1] < 100, compMax))  #retira um valor máximo do indice [1] da lista 'compMax'
duasEst = list(filter(lambda valMax: valMax[1] > 100 and valMax[1] <=200, compMax))
tresEst = list(filter(lambda valMax: valMax[1] > 200 and valMax[1] <=300, compMax))

print(f'Uma estrela: {umaEst[0][0]} - Max passageiros: {umaEst[0][1]}')
print(f'Duas estrelas: {duasEst[0][0]} - Max passageiros: {duasEst[0][1]}')
print(f'Três estrelas: {tresEst[0][0]} - Max passageiros: {tresEst[0][1]}')

#esse modelo só funcionou, pois só há 1 companhia por estrela, caso houvessem mais companhias, deveria criar novos
#modelos de comparação para encaixar cada companhia em sua quantidade de estrela

