"""
EXERCÍCIOS DE SORTED AND REVERSED:
1- Receba números inteiros do usuário e armazene-os em uma lista. Crie uma condição para o número 0 finalizar o processo
de preenchimento. Após isso, imprima o maior valor da lista utilizando as funções sorted() e len(). Por fim, utilize
reversed() para inverter a lista e obtenha, pelo indice, o valor intermediário da mesma.
OBS.: Caso o número de valores da lista seja par, pegue a média dos dois valores centrais.

RESULTADO:



"""
num = 1
listaNum = []
while num != 0:
    num = int(input('Digite um número inteiro: '))
    if num != 0:
        listaNum.append(num)

ordenada = sorted(listaNum)
tamanho = len(listaNum)

print(f'Maior valor: {ordenada[tamanho -1]}')   #o maior valor é o último indice (elemento - 1), pois começa do 0 e não do 1.

invertida = reversed(listaNum)
listaInvertida = list(invertida)

if tamanho % 2 == 1:
    print(f'Valor intermediário: {listaInvertida[tamanho // 2]}')
else:
    print(f'Valor intermediário: {(listaInvertida[tamanho // 2] + listaInvertida[(tamanho // 2) - 1]) /2}')
