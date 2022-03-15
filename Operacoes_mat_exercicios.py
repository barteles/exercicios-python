""""""
"""
Exercicio de operações matemáticas
1- Realizar a média de 4 alunos
2-Converter uma temperatura de graus °C para °F e para °K.
Dados: °F= °C*1,8 + 32, °K= °C + 273

RESPOSTA;
1) 
med1 = float(input('insira a média do aluno 01: '))
med2 = float(input('Insira a média do aluno 02: '))
med3 = float(input('Insira a média do aluno 03: '))
med4 = float(input('Insira a média do aluno 04: '))

print(f'A média dos 4 alunos é: {(med1 + med2 + med3 + med4) / 4}')

OU
med1 = float(input('insira a média do aluno 01: '))
med2 = float(input('Insira a média do aluno 02: '))
med3 = float(input('Insira a média do aluno 03: '))
med4 = float(input('Insira a média do aluno 04: '))

media = (med1 + med2 + med3 + med4) / 4
print(f' a media é: {media})

#__________________________________________________________________________________________________________

2)
temp = float(input('Insira a temperatura em °C: '))
print(f'A temperatura em °F é: {temp * 1.8 + 32}°F')
print(f'A temperatura em °K é: {temp + 273.15}°K')

OU
tempC = float(input('insira a temperatura em °C: '))
tempF = tempC * 1.8 + 32
tempK = tempC + 273.15
print(f'A temperatura de {tempC}°C em °F é: {tempF}°F')
print(f'A temperatura de {tempC}°C em °K é: {tempK}°F')

#__________________________________________________________________________________________________________

EXERCÍCIOS DE SEÇÃO:
1- Descubra quais são os erros nesses códigos:
a) nome = 'Mark '
print(int(nome))

b) frase = 'Eu sou seu pai'
print(frase[-1::]

c) filme = 'Avatar'
print('A maior bilheteria de 2009 foi o filme {filme}')

d)numerol = 10
dado = int(input(Digite o número que deseja: ))
print(numerol * dado)

#__________________________________________________________________________________________________________

2- Criação de personagem  de mundo de ficção, apresentando opções de acordo com os tipos de variáveis:
- Cor do cabelo (string)
- Cor da pele (string)
- Classe: mago, guerreiro, Arqueiro (string)
- Idade (int)
- Altura (float)
- Habilidade Específica (string)
Imprima ao usuário o seu  personagem completo


RESPOSTAS:
1-a) Ele transforma uma string em um número inteiro, porém como não há números na variável, o python apresenta erro.

b) a função [-1::] traz somente o número de digitos da frase vindo da direita para a esquerda, ou seja,
caso queira a palavra pai por exemplo será [-3::], caso o objetivo seja a frase ao contrário deveria estar: [::-1]

c) neste caso, está faltando o 'f' em print(f'...') e portanto ele não reconhece que {filme} é uma variável

d) O erro aqui é que não foi digitado as aspas do input


2- #mensagens iniciais
print('-------Bem vindo a um novo universo-------\n\n')

print('--------Crie o seu personagem----------\n\n')

#entrada de dados pelo usuário
cabelo = input('Digite a cor do cabelo do seu personagem: ')
corPele = input('Digite a cor da pele do seu personagem: ')
classe = input('Escolha a sua classe: \n1- Guerreiro\n2 - Mago\n3 - Arqueiro\nOpção: ')
idade = int(input('Digite a idade do seu personagem em anos: '))
altura = float(input('Digite a altura em metros do seu personagem: '))
HabEspecial = input('Digite a habilidade especial do seu personagem: ')

print('\n\n-------Personagem criado-------\n\n')
#impressão completa do personagem
print(f'O seu personagem tem: \n'
      f'Cor de cabelo: {cabelo}\n'
      f'Cor de pele: {corPele}\n'
      f'classe: {classe}\n'
      f'idade: {idade} anos\n'
      f'altura: {altura}m\n'
      f'habilidade de: {HabEspecial}')

print('\n\n------Deseja continuar?------')
"""

nota = float(input('Digite sua nota: '))

if nota > 6 and nota < 9:
    print('Muito bem Aproveite suas férias')
elif nota == 6:
    print('Aproveite suas férias')
elif nota > 9:
    print('Parabéns, você tirou nota máxima')
else :
    print('Reprovado')

