"""
EXERCICIO ARQUIVOS CSV:
1- Um time de futsal formado pelo arquivo atletas.csv, que contém o nome, altura(cm) e peso(kg) de cada esportista, deseja
fazer uma pesquisa e saber quais atletas tem altura superior a 170cm e que possui peso menor que 80kg, imprima o nome deles.
Dois reforços entraram para o time no início da temporada, Roberto, 175, 77kg e Adriana, 165, 66kg. Atualize o arquivo
adicionando os jogadores e leia-o novamente.

RESULTADO:
from csv import reader
from csv import writer

with open('atletas.csv') as arq:
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        if int(linha[1]) > 170 and int(linha[2]) < 80:
            print(linha[0])

with open('atletas.csv', 'a+', newline= '') as arq: #newline é para evitar espaços entre as informações adicionadas posteriormente
    escrita = writer(arq)
    escrita.writerow(['Roberto', 175, 77])
    escrita.writerow(['Adriana', 165, 66])
    arq.seek(0) #deve retornar para a posição 0 para iniciar a leitura, pois os append jogam o cursor para o final do arquivo
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        print(linha)

#_______________________________________________________________________________________________________________________
EXERCÍCIOS PICKLE/ JSON:
2-Deseja-se criar um programa que deixe a fórmula secreta da coca-cola criptografada, para isso crie uma classe
FormulaCocaCola com atributos privados: ingrediente, temperatura (celsius), açucar (gramas), e o nome do proprietário.
Crie uma senha de acesso escolhida pelo usuário, instancie o objeto e passe o mesmo para um arquivo PICKLE. Após isso,
peça a senha para acessar os atributos, caso seja correta, leia o arquivo e imprima-os, se não, imprima um aviso de
acesso negado.

RESULTADO:
import pickle

class FormulaCocaCola:
    def __init__(self, ingrediente, temperatura, acucar, proprietario):
        self.__ingrediente = ingrediente
        self.__temperatura = temperatura
        self.__acucar = acucar
        self.__proprietario = proprietario

    @property
    def ingrediente(self):
        return self.__ingrediente

    @property
    def temperatura(self):
        return self.__temperatura

    @property
    def acucar(self):
        return self.__acucar

    @property
    def proprietario(self):
        return self.__proprietario

coca_cola = FormulaCocaCola('agua gaseificada', 5, 9, 'Asa Griggs Candler')
cria_senha = input('Digite a senha que deseja criar: ')

with open('receita_secreta.pickle', 'wb') as arq:   #'wb' é escrita em binário
    pickle.dump(coca_cola,arq)     #dump() serve para codificar em binário pelo pickle

senha = input('Digite a senha para acessar a fórmula secreta: ')

if senha == cria_senha:
    print('__________Acesso Permitido__________')
    with open('receita_secreta.pickle', 'rb') as arq:
        coca_cola = pickle.load(arq)
        print(f'Ingrediente: {coca_cola.ingrediente}')
        print(f'Temperatura para produção: {coca_cola.temperatura}°C')
        print(f'Quantidade de acuçar: {coca_cola.acucar} gramas')
        print(f'Dono da receita: {coca_cola.proprietario}')
else:
    print('_______________Acesso Negado_______________')
    print('Intruso!! Alarmes ativados!')


#_______________________________________________________________________________________________________________________
EXERCICIO FIM DE SEÇÃO CSV, PICKLE, JSON
3- Crie dois arquivos: um em CSV e um JSONPICKLE. Escreva as lucros de uma empresa em um balanço trimestral, apresentando
o mês e o lucro de milhões no CSV, e as despesas nos mesmos meses em JSONPICKLE a partir dos objetos criados em uma classe
chamada Empresa. Após isso, troque seus conteúdos, ou seja, armazene os valores dos lucros no JSONPICKLE e os valores
das despesas no CSV.

"""
from csv import writer, reader
import jsonpickle

class Empresa:
    def __init__(self, mes, dinheiro):
        self.__mes = mes
        self.__dinheiro = dinheiro

    @property
    def dinheiro(self):
        return self.__dinheiro
    @dinheiro.setter    #decorador que me permite modificar o valor de dinheiro
    def dinheiro(self,novo_dinheiro):
        self.__dinheiro = novo_dinheiro

janeiro = Empresa('Janeiro', 4)
fevereiro = Empresa('Fevereiro', 6)
marco = Empresa('Marco', 7)

with open('lucros.csv', 'w', newline= '', encoding='utf-8') as arq:
    escrita = writer(arq, delimiter = ':')
    escrita.writerow(['Mês', 'Lucro( Milhões)'])
    escrita.writerow(['Janeiro', 10])
    escrita.writerow(['Fevereiro', 3])
    escrita.writerow(['Marco', 11])

list = []   #criei uma lista vazia que irá receber meus 3 objetos e assim ser 1 único elemento a ser codificado pelo json
list.append(janeiro)
list.append(fevereiro)
list.append(marco)

with open('despesas.json', 'w') as arq:
    arq.write(jsonpickle.encode(list))  #aqui irei escrever e codificar em json a lista dos 3 objetos

despesas = []
lucros = []

with open('lucros.csv') as arq_csv:
    with open('despesas.json') as arq_jsonpickle:
        #obtenção dos dados JSON
        list = jsonpickle.decode(arq_jsonpickle.read())
        #leitura do primeiro objeto
        janeiro = list[0]
        #leitura do segundo objeto
        fevereiro = list[1]
        #leitura do terceiro objeto
        marco = list[2]
        #adicionando os objetos na lista despesa
        despesas.append(janeiro.dinheiro)
        despesas.append(fevereiro.dinheiro)
        despesas.append(marco.dinheiro)
        #Obtenção dos dados CSV
        leitura = reader(arq_csv, delimiter = ':')
        next(leitura)   #pular cabeçalho
        for linha in leitura:
            lucros.append(linha[1])

with open('lucros.csv', 'w', newline='', encoding='utf-8') as arq_csv:  #aqui irei atualizar lucros com os valores de despesas
    escrita = writer(arq_csv)
    escrita.writerow(['Mês', 'Lucro( Milhões)'])
    escrita.writerow(['Janeiro', despesas[0]])
    escrita.writerow(['Fevereiro', despesas[1]])
    escrita.writerow(['Marco', despesas[2]])

with open('despesas.json', 'w') as arq_jsonpickle:  #aqui irei atualizar despesas com os valores de lucros
    janeiro.dinheiro = lucros[0]    #a variável janeiro deve receber o valor de lucros[0 = 10 milhoes
    fevereiro.dinheiro = lucros[1]
    marco.dinheiro = lucros[2]
    list = []
    list.append(janeiro)
    list.append(fevereiro)
    list.append(marco)
    arq_jsonpickle.write(jsonpickle.encode(list))