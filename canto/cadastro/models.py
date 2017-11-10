# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Funcionario(models.Model):
	nome = models.CharField(max_length=300)
	salario = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	hora_extra = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	vale_transporte = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	unimed = models.DecimalField(max_digits=8, decimal_places=2, default=0)

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome

@python_2_unicode_compatible
class Entrada(models.Model):
	nome = models.CharField(max_length=300)

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome		

@python_2_unicode_compatible
class SaidaGrupo(models.Model):

	class Meta:
		verbose_name_plural = 'Contas de Saída - Grupos'		
		verbose_name = 'Conta de Saída - Grupo'	

	nome = models.CharField(max_length=300)

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome				

@python_2_unicode_compatible
class SaidaSubgrupo(models.Model):

	class Meta:
		verbose_name_plural = 'Saída - Subgrupos'		
		verbose_name = 'Subgrupo'	

	nome = models.CharField(max_length=300)
	grupo = models.ForeignKey(SaidaGrupo)

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome				

@python_2_unicode_compatible
class Saida(models.Model):
	nome = models.CharField(max_length=300)
	grupo = models.ForeignKey(SaidaGrupo)
	subgrupo = models.ForeignKey(SaidaSubgrupo)	

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome				