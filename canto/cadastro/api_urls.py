# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
     url(r'^entradas/$', views.entradas_json, name='api-entradas-json'),
     url(r'^entrada/delete/(?P<pk>[0-9]+)$', views.exclui_entrada_json, name='api-entradas-delete'),
]