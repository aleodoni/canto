from django.contrib import admin

from .models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
	model = Funcionario
	list_per_page = 20
	ordering = ('nome',)
	search_fields = ('nome', )

admin.site.register(Funcionario, FuncionarioAdmin)