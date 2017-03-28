from django.test import TestCase

from ..models import Funcionario

from django.db import IntegrityError, DataError


class FuncionarioModelTest(TestCase):

    def setUp(self):
        self.funcionario = Funcionario.objects.create(nome='Zaca')

    def test_string_representation(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Funcionario._meta.verbose_name_plural), "funcionarios")

    def test_nome_branco(self):
        with self.assertRaises(IntegrityError):
            funcionario = Funcionario.objects.create(nome=None)

    def test_nome_maior_300(self):
    	with self.assertRaises(DataError):
    	    funcionario = Funcionario.objects.create(nome='A' * 301)