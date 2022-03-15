"""
Exercício de variáveis

1- elabore um código que peça o nome do aluno e sua nota e os retorna numa única linha de código.
Além disso, utilize a função title().
"""

Nome = input('Digite o nome do/a aluno/a: ')            # insere o nome do aluno
Nota = input('Digite a nota do aluno/a: ')              # insere a nota desse aluno
print(f'O aluno: {Nome.title()} tirou a nota: {Nota}')  # imprimi em uma única linha de código nome e nota
