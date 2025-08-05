from django.urls import path
from . import views

urlpatterns = [
    path('hospedes', views.listar_hospedes, name='listar_hospedes'),
    path('novo-hospede/', views.cadastrar_hospede, name='cadastrar_hospede'),
    path('editar-hospede/<int:cpf>/', views.editar_hospede, name='editar_hospede'),
    path('deletar-hospede/<int:cpf>/', views.deletar_hospede, name='deletar_hospede'),
]