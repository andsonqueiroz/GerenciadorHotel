from django.urls import path
from . import views

urlpatterns = [
    path('criar_servico/', views.criar_servico, name='criar_servico'),
    path('editar_servico/<int:id>', views.editar_servico, name='editar_servico'),
    path('deletar_servico/<int:id>', views.deletar_servico, name='deletar_servico'),
    path('listar_servicos/', views.listar_servicos, name='listar_servicos'),
]