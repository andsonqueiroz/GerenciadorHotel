from django.shortcuts import render, redirect, get_object_or_404
from .forms import FuncionarioForm
from .models import Funcionario

def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')  
    else:
        form = FuncionarioForm()

    return render(request, 'funcionarios/form.html', {'form': form})

def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
      form = FuncionarioForm(request.POST, instance=funcionario)
      if form.is_valid():
         form.save()
         return redirect('listar_funcionarios')
    else:
      form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionarios/form.html', {'form': form})
    

def deletar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id = id)
    funcionario.delete()
    return redirect('listar_funcionarios')

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/listar_funcionarios.html', {'funcionarios': funcionarios})