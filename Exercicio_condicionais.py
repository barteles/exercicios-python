""""""
"""
Exercício de Condicionais
1- Fazer uma calculadora com 4 operações (soma, multiplicação, divisão inteira, potenciação)
Peça a operação desejada e depois os dois números ao usuário.
"""
#mensagem inicial
print('-------Olá, eu sou sua calculadora-------')
print('-------Escolha a opção desejada:-------')
operacao = int(input('1- Soma\n'
      '2- Multiplicação\n'
      '3- divisão inteira\n'
      '4- potenciação\n opçao: '))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('-------Resultado:-------')
if operacao == 1:
    print(f'Soma: {num1 + num2}')
elif operacao == 2:
    print(f'Multiplicação: {num1 * num2}')
elif operacao == 3:
    print(f'Divisão inteira: {num1 // num2}')
elif operacao == 4:
    print(f'Potenciação: {num1 ** num2}')
else:
    print('Digite uma opção válida')
