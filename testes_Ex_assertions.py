"""
TESTES DOS EXERCICIOS DE ASSERTIONS

1-

import unittest
from Exercicio_Assertions import acordar_cedo, tempo_exercicio, tem_execicio

class ExAssertionsTestes(unittest.TestCase):

    def test_acordar_cedo_tipo(self):
        self.assertIs(type(acordar_cedo(10)), str, 'Não é uma string')

    def test_acordar_cedo_falha(self):
        self.assertEqual(acordar_cedo(10), 'Tente novamente amanhã') #testa se caso acorde após as 6h, irá retornar
        # 'tente novamente''

    def test_acordar_cedo_concluido(self):
        self.assertEqual(acordar_cedo(5), 'Você é um guerreiro')

    def test_tempo_exercicio_concluido(self):
        self.assertEqual(tempo_exercicio(3, 67), 66)

    def test_tempo_exercicio_falha(self):
        self.assertIsNone(tempo_exercicio(1,67))

    def test_tem_exercicio_negativo(self):
        self.assertFalse(tem_execicio('Descanso'))

    def test_tem_exercicio_positivo(self):
        self.assertTrue(tem_execicio('Natação'))

if __name__ == '__main__':
    unittest.main()

------------------------------------------------------------------------------------------------------------------------

2-
from Exercicio_Assertions import Tatu
import unittest

class ExAssertions3Teste(unittest.TestCase):

    def setUp(self):
        self.bola = Tatu('Bola')
        self.napoleao = Tatu('Napoleão')

    def test_comer(self):
        self.assertEqual(self.bola.comer(), 'sou o Bola e estou comendo pizza')

    def test_beber(self):
        self.assertEqual(self.bola.beber(), 'sou o Bola e estou bebendo suco')

    def test_acasalar(self):
        self.assertEqual(self.bola.acasalar(), 'sou o Bola e quero um filhote')

    def tearDown(self):
        print('Teste concluido')

if __name__ == '__main__':
    unittest.main()


________________________________________________________________________________________________________________________

5-


"""
from Exercicio_Secao_Testes_TDD_Doctest import Mulher
import unittest

class ExerciciosSecaoTesteMulher(unittest.TestCase):

    def setUp(self):
        self.ana = Mulher('Ana', 60, 123456, 28)
        self.vanessa = Mulher('Vanessa', 60, 123456, 8)

    def test_aposentadoria_completa(self):
        self.assertEqual(self.ana.aposentadoria(), 'Voce pode se aposentar')

    def test_aposentadoria_falha(self):
        self.assertEqual(self.vanessa.aposentadoria(),'Ainda nao atingiu os requisitos para se aposentar')

    def tesst_salario_aposentadoria_falha(self):
        self.assertEqual(self.vanessa.salario_aposentadoria(), 'Voce nao nao pode se aposentar')

    def test_salario_aposentadoria_completo(self):
        self.assertEqual(self.ana.salario_aposentadoria(),3600)

if __name__ == '__main__':
    unittest.main()