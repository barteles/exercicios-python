"""
EXERCICIO DUNDER NAME, DUNDER MAIN:
1- Crie uma pasta e uma subpasta, em seguida um módulo nessa subpasta contendo uma função qualquer. Acesse o módulo no
programa principal e execute a função
Obs.: No módulo criado, estabeleça a condição para a função ser acessada apenas se o módulo for importado e executado em outro.
Ou seja, quando o módulo em questão não é o principal (main).

RESULTADO>
from PacoteFora.PacoteDentro.Modulo_dentro import preverFuturo
from random import choice as ch


idades = [12, 65, 73, 44, 57, 84, 4, 8, 26, 18, 21, 13, 25, 22, 15, 67]
formacao = ['Filosofia', 'engenharia', 'medicina', 'artes', 'letras', 'biologia']
trabalho = ['bartender', 'politico(a)', 'administrador(a)', 'professor(a)', 'carpinteiro(a)']
pais = ['França', 'Angola', 'Escócia', 'Espanha', 'Turquia']
animal = ['crocodilo', 'urso', 'sapo', 'elefante', 'tubarão', 'golfinho']
nome = input('Digite um nome: ')

preverFuturo(nome, ch(idades), ch(formacao), ch(trabalho), ch(pais), ch(animal))

"""

"""
EXERCÍCIO DE SEÇÃO:
1- Maria e Joao estão jogando bingo em família. Cada um possui uma cartela e cada cartela possui 7 numeros de 1 a 30,
que serão sorteados por uma função, utilizando choice(), contida em um módulo customizado, sendo acessada apenas se o 
módulo for importado. Os números das cartelas devem ser definidos utilizando comprehensions e choices() no programa principal.
O primeiro a ter seus 7 numeros chamados vence. Crie um sistema para representar o jogo, como os números sorteados e a conferência
das cartelas. No final apresente o vencedor, os números das cartela do vencedor e os números sorteados.

RESULTADO:

"""
from random import choice as ch
from Exercicios.Modulo_exercicio_bingo_secao import sorteio

numeros = 7 #quantidade de numeros de cada cartela
max = 30    #limite de números do sorteio.

sorteador = list(range(1, max + 1))
cartelaMaria = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]
#define números aleatórios para a cartela de maria de 1 a 30.

sorteador = list(range(1, max + 1))
cartelaJoao = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]
#Escolhe um número da lista 'Sorteador'. O número escolhido é depois remodivo dessa lista para não haver repetições
#nos números sorteados. Como o pop() retorna o número removido, ele é adicionado na cartela de João ou na de Maria

sorteio(cartelaJoao, cartelaMaria, max)
