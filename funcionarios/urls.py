from django.urls import path
from . import views

urlpatterns = [
    path('criar_funcionario/', views.criar_funcionario, name='criar_funcionario'),
    path('editar_funcionario/<int:id>', views.editar_funcionario, name='editar_funcionario'),
    path('deletar_funcionario/<int:id>', views.deletar_funcionario, name='deletar_funcionario'),
    path('listar_funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
]