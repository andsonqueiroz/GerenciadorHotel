from django.shortcuts import render, redirect, get_object_or_404
from .models import Hospede
from .forms import HospedeForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_hospedes(request):
    hospedes = Hospede.objects.all()
    return render(request, 'hospedes/listar.html', {'hospedes': hospedes})

@login_required
def cadastrar_hospede(request):
    if request.method == 'POST':
        form = HospedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_hospedes')
    else:
        form = HospedeForm()
    return render(request, 'hospedes/form.html', {'form': form})

@login_required
def editar_hospede(request, cpf):
    hospede = get_object_or_404(Hospede, cpf=cpf)
    form = HospedeForm(request.POST or None, instance=hospede)
    if form.is_valid():
        form.save()
        return redirect('listar_hospedes')
    return render(request, 'hospedes/form.html', {'form': form})

@login_required
def deletar_hospede(request, cpf):
    hospede = get_object_or_404(Hospede, cpf=cpf)
    hospede.delete()
    return redirect('listar_hospedes')