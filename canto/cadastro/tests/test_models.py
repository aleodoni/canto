from django.test import TestCase

from ..models import Funcionario, Entrada, SaidaGrupo, SaidaSubgrupo, Saida

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


class EntradaModelTest(TestCase):

    def setUp(self):
        super(EntradaModelTest, self).setUp()

    def test_dummy(self):
        self.assertEqual(1,1)

    def test_nome_branco(self):
        with self.assertRaises(IntegrityError):
            entrada = Entrada.objects.create(nome=None)


class SaidaGrupoModelTest(TestCase):

    def setUp(self):
        super(SaidaGrupoModelTest, self).setUp()

    def test_dummy(self):
        self.assertEqual(1,1)

    def test_nome_branco(self):
        with self.assertRaises(IntegrityError):
            grupo = SaidaGrupo.objects.create(nome=None)            


class SaidaSubgrupoModelTest(TestCase):

    def setUp(self):
        super(SaidaSubgrupoModelTest, self).setUp()

    def test_dummy(self):
        self.assertEqual(1,1)

    def test_nome_branco(self):
        with self.assertRaises(IntegrityError):
            subgrupo = SaidaSubgrupo.objects.create(nome=None)                        

    def test_grupo_branco(self):
        with self.assertRaises(IntegrityError):
            subgrupo = SaidaSubgrupo.objects.create(nome='Teste', grupo=None)


class SaidaModelTest(TestCase):

    def setUp(self):
        super(SaidaModelTest, self).setUp()

    def test_dummy(self):
        self.assertEqual(1,1)

    def test_nome_branco(self):
        with self.assertRaises(IntegrityError):
            saida = Saida.objects.create(nome=None)                        

    def test_grupo_branco(self):
        with self.assertRaises(IntegrityError):
            saida = Saida.objects.create(nome='Teste', grupo=None)            

    def test_subgrupo_branco(self):
        grupo = SaidaGrupo.objects.create(nome='Saida Grupo')
        with self.assertRaises(IntegrityError):
            saida = Saida.objects.create(nome='Teste', grupo=grupo, subgrupo=None)