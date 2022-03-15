""""""
"""
EXERCÍCIO MÓDULOS EXTERNOS CUSTOMIZADOS:
1- Criar um módulo customizado com duas funções (cálculo de quantidade de números pares e impares em uma lista qualquer).
Em seguida, execute as funções passando como argumento uma lista de números inteiros

"""
from modulo import(
   countpares as cp,
   contaImpar as ci
)

lista = [10, 8, 9, 21, 33, 44,  12, 7, 6 , 5, 3, 4, 2]


print(cp(lista))
print(ci(lista))