from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.listar_tudo, name='listar_tudo'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]