from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.generic.edit import FormView, CreateView, UpdateView

from .models import Entrada
from .forms import EntradaForm


class EntradaIndexView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'cadastro/entrada/index.html'

class EntradaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Entrada
	form_class = EntradaForm
	success_url = '/cadastro/entrada/'
	success_message = "Conta de Entrada criada com sucesso"
	template_name = 'cadastro/entrada/create.html'	

class EntradaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Entrada
	form_class = EntradaForm
	success_url = '/cadastro/entrada/'
	success_message = "Conta de Entrada alterada com sucesso"
	template_name = 'cadastro/entrada/update.html'		    



def entradas_json(request):
	resposta = []

	entradas = Entrada.objects.all().order_by('nome')

	for e in entradas:
		entrada_json = {}
		entrada_json['id'] = e.id
		entrada_json['nome'] = e.nome
		resposta.append(entrada_json)
	return JsonResponse(resposta, safe=False)           

def exclui_entrada_json(request, pk):
    if request.method == 'POST' and request.is_ajax():
        if pk != None and pk != '':
            entrada = Entrada.objects.get(pk=pk)
            entrada.delete()
            response = JsonResponse({'status':'true','message':'Conta de Entrada excluída com sucesso'}, status=200)
        else:
            response = JsonResponse({'status':'false','message':'Erro ao excluir Conta de Entrada'}, status=401)
    else:
        response = JsonResponse({'status':'false','message':'Não foi possível localizar a Conta de Entrada'}, status=401)
    return response    		