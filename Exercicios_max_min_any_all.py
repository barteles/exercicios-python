""""
EXERCÍCIO MAX, MIN, ANY ALL:
1- Criar uma lista e uma tupla com diversos valores, separar valores máximos e mínimos de cada uma em um conjunto.
Por fim, verificar se os 4 valores separados sao verdadeiros ou falsos utilizando any e o all.
"""

lista = [11, 34, 23, 345, 100, 2340, -345, 45]
tupla = (True,5,21,0, 350, 34, 125, 234)

conjunto = {max(lista), min(lista), max(tupla), min(tupla)}
print(conjunto)

print(any(conjunto))    #Há pelo menos 1 valor True? R: Sim, logo retorna True
print(all(conjunto))    #Todos os valores são True? R: Não, logo a resposta é False

