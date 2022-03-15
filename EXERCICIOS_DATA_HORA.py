"""
EXERCÍCIO COM FORMATAÇÃO DE DATA E HORA
1- Dudu é um famosinho do instagram e precisa manter as postagens em seu Feed regularmente. Portanto, teve a ideia de criar
um programa em Python que agende suas publicações para todas as segundas, quartas e sextas ao longo de um mês, a partir
desse momento. Além disso, seus posts irão variar entre os temas: saúde, vida pessoal e motivacional. Com isso, utilize
choice() para selecionar cada conteúdo aleatóriamente. Faça um programa que implemente a ideia de Dudu, imprimindo o
conteúdo de cada um dos dias e suas respectivas dias de postagens.

RESULTADO:


"""
import datetime
from random import choice as ch

temas = ['Saúde', 'Vida pessoal', 'Motivacional']
este_momento = datetime.datetime.now()
print(este_momento)
print(repr(este_momento))

mesQueVem = este_momento + datetime.timedelta(30)   #dia atual recebendo mais 30 dias, tendo o intervalo de tempo de 1 mês
print(mesQueVem)
print(repr(mesQueVem))
print('\n')

while (este_momento.day <= mesQueVem.day) or (este_momento.month < mesQueVem.month):
    #primeiro verifica se o mês atual é menor que o mes do mesQueVem, a partir do momento que essa for falsa, verifica se
    #o dia atual é menor que o dia do mesQueVem.
    if este_momento.weekday() == 0:
        print(f'Segunda feira, {este_momento}. Tema: {ch(temas)}')
    elif este_momento.weekday() == 2:
        print(f'Quarta feira, {este_momento}. Tema: {ch(temas)}')
    elif este_momento.weekday() ==4:
        print(f'Sexta feira, {este_momento}. Tema: {ch(temas)}\n')

    este_momento += datetime.timedelta(1)   #aumenta em um dia o dia atual