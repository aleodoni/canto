from django.contrib import admin

from .models import Funcionario, SaidaGrupo, SaidaSubgrupo, Entrada, Saida

class SaidaInline(admin.TabularInline):
	model = Saida
	extra = 2

class SaidaSubgrupoInline(admin.TabularInline):
	model = SaidaSubgrupo
	extra = 2
	
class FuncionarioAdmin(admin.ModelAdmin):
	model = Funcionario
	list_per_page = 20
	ordering = ('nome',)
	search_fields = ('nome', )

class EntradaAdmin(admin.ModelAdmin):
	model = Entrada
	ordering = ('nome', )
	search_fields = ('nome', )

class SaidaGrupoAdmin(admin.ModelAdmin):
	model = SaidaGrupo
	ordering = ('nome', )
	search_fields = ('nome', )
	inlines = [SaidaSubgrupoInline]	

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(SaidaGrupo, SaidaGrupoAdmin)
admin.site.register(Saida)