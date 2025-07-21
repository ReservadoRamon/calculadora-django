from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculadora, name='calculadora'),
    path('limpar/', views.limpar_historico, name='limpar_historico'),
]