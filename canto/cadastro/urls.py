# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'entrada/$', views.EntradaIndexView.as_view(), name='index-entrada'),
    url(r'^entrada/new/$', views.EntradaCreateView.as_view(), name='entrada-new'),
    url(r'^entrada/edit/(?P<pk>[0-9]+)/$', views.EntradaUpdateView.as_view(), name='entrada-edit'),
    url(r'^api/entradas/$', views.entradas_json, name='api-entradas-json'),
]