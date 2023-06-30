from django.urls import include, path
from rest_framework import routers
from api import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('nome/', views.NomeView.as_view(), name='nome'),
    path('nome_completo/', views.NomeCompletoView.as_view(), name='nome_completo'),
    path('nome_com_filiacao/', views.NomeComFiliacaoView.as_view(),
         name='nome_com_filiacao'),

    path('cpf/', views.CPFView.as_view(), name="cpf"),

    path('rg/', views.RGView.as_view(), name="rg"),

    path('auth/', include('rest_framework.urls')),
]
