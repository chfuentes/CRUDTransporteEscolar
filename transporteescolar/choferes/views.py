from django.shortcuts import render, redirect, get_object_or_404
from .models import Chofer
from .forms import ChoferForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/usuarios/login")
def registrar_chofer(request):
    if request.method == 'POST':
        form = ChoferForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Chofer registrado exitosamente.')
            return redirect('choferes:listar_choferes')
    else:
        form = ChoferForm()
    return render(request, 'choferes/registrar_chofer.html', {'form': form})


@login_required(login_url="/usuarios/login")
def listar_choferes(request):
    choferes = Chofer.objects.all()
    return render(request, 'choferes/listar_choferes.html', {'choferes': choferes})


@login_required(login_url="/usuarios/login")
def editar_chofer(request, id):
    chofer = get_object_or_404(Chofer, id=id)
    if request.method == 'POST':
        form = ChoferForm(request.POST, instance=chofer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Chofer actualizado exitosamente.')
            return redirect('choferes:listar_choferes')
    else:
        form = ChoferForm(instance=chofer)
    return render(request, 'choferes/editar_chofer.html', {'form': form, 'chofer': chofer})


@login_required(login_url="/usuarios/login")
def eliminar_chofer(request, id):
    chofer = get_object_or_404(Chofer, id=id)
    if request.method == 'POST':
        chofer.delete()
        messages.success(request, 'Chofer eliminado exitosamente.')
        return redirect('choferes:listar_choferes')
    return render(request, 'choferes/eliminar_chofer.html', {'chofer': chofer})
