# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import get_user_model


from ..models import Funcionario
from ..views import EntradaIndexView

class FuncionarioAdminViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='admin')
        self.user.set_password('admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.save()
   
    def test_login(self):
    	client = Client()
    	logged_in = client.login(username='admin', password='admin')

    def test_admin_funcionario(self):
    	client = Client()
    	client.login(username='admin', password='admin')
    	response = client.get('/admin/cadastro/funcionario/')
    	self.assertEqual(response.status_code, 200)

    def test_uma_entrada(self):
    	Funcionario.objects.create(nome='Zaquinha')
    	client = Client()
    	client.login(username='admin', password='admin')
    	response = client.get('/admin/cadastro/funcionario/')
    	self.assertContains(response, 'Zaquinha')

    def test_duas_entrada(self):
    	Funcionario.objects.create(nome='Zaquinha')
    	Funcionario.objects.create(nome='Nosferatu')
    	client = Client()
    	client.login(username='admin', password='admin')
    	response = client.get('/admin/cadastro/funcionario/')
    	self.assertContains(response, 'Zaquinha')
    	self.assertContains(response, 'Nosferatu')

    def test_sem_entrada(self):
    	client = Client()
    	client.login(username='admin', password='admin')
    	response = client.get('/admin/cadastro/funcionario/')
    	self.assertContains(response, '0 funcionarios')


class EntradaViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user("zaca", "zaca")
        self.user.is_staff = True
        self.user.save()

    def test_index_vazio(self):
        request = self.factory.get('/cadastro/entrada/')
        request.user = self.user
        response = EntradaIndexView.as_view()(request)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contas de Entrada')
        self.assertContains(response, 'Sem contas de entrada cadastradas')        