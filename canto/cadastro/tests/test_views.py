# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.contrib.auth import get_user_model


from ..models import Funcionario

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