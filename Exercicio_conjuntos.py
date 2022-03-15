"""
EXERCÍCIO DE CONJUNTOS(SETS):
1- Sami e Dudu irão fazer uma competição de quem visita mais Estados do Brasil em um período de 6 meses. Até então,
Dudu visitou Espirito Santo e São Paulo, enquanto que Sami visitou Rio de Janeiro e Bahia. Crie dois conjuntos
diferentes para simbolizar os estados que cada um foi. Após seis meses Dudu visitou Bahia, Acre, Santa Catarina e
Sergipe, equanto que Sami visitou Bahia, Minas Gerais, Amazonas e Paraná. Atualize cada um dos conjuntos com os novos
estados e responda:
 - Quais estados Dudu visitou que Sami não foi?
 - Quais estados ambos foram?
 - Sendo 27 estados no Brasil todo, qual a percentagem o vencedor visitou?

RESULTAOD:
Sami = {'RJ', 'BA'}
Dudu = {'SP', 'ES'}
sair = ''

#após 6 meses, dar update
while sair != 'nao':
    Sami.add(input('\nQual estado Sami visitou a mais?: '))
    sair = input('tem mais algum estado a adcionar?')

sair = ''
while sair != 'nao':
    Dudu.add(input('\nQual estado Dudu visitou a mais?: '))
    sair = input('tem mais algum estado a adcionar?')

#Quais estados Dudu visitou que Sami não?
print(Dudu.difference(Sami))

#Quasi estados ambos foram?
print(Dudu.intersection((Sami)))

#Para saber quem visitou mais estados e qual a percentagem de estados visitados:
if len(Dudu) > len(Sami):
    print(f'Dudu ganhou e visitou: {len(Dudu)*100 // 27}%')
elif len(Sami) > len(Dudu):
    print(f'Sami ganhou e visitou: {len(Sami) * 100 // 27}%')
else:
    print(f'Deu empate e visitaram: {len(Sami) * 100 // 27}%')

#__________________________________________________________________________________________________________

SET COMPREHENSION EXERCÍCIO:
1- Pra cada número numa range de 1 a 9, adicione esse número elevado ao quadrado no conjunto, se o número for
impar adicione 2 elementos, 1 por vez: 'Sou' e 'impar'. Qual foi a resposta? Por que 'Sou', 'impar' só apareceu
uma vez?

RESULTADO:
Ele aparece somente uma vez, pois conjuntos não aceitam elementos repetidos.

#aqui está como deve ser montado
conjunto = set({})

for number in range(1,10):
    if number %2 ==0:
        conjunto.add(number**2)
    else:       #nesse entrarão no loop: 1, 3, 5, 7 e 9
        for num in range(0,2)   #para cada numero que entrou ele fará um loop retornando o 0 e 1 para adc as palavras
            if num ==0:     #'Sou' e 'impar', ou seja, 1 = 0 -> Sou 1 -> impar, 3 = 0->Sou 1 ->impar, 5 = 0-> Sou 1-> impar,...
                conjunto.add('Sou')
            else:
                conjunto.add('Impar')
print(conjunto)

#aqui está como comprehension (o segundo for deve estar dentro do primeiro for)
conjunto = {number ** 2 if number % 2 == 0 else 'Sou' if num ==0 else 'impar' for num in range(0,2) for number in range(1,10)}
print(conjunto)

"""
