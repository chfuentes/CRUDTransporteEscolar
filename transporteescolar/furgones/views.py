from django.shortcuts import render, redirect, get_object_or_404
from .models import Furgon
from .forms import FurgonForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/usuarios/login")
def registrar_furgon(request):
    if request.method == 'POST':
        form = FurgonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Furgón registrado exitosamente.')
            return redirect('furgones:listar_furgones')
    else:
        form = FurgonForm()
    return render(request, 'furgones/registrar_furgon.html', {'form': form})


@login_required(login_url="/usuarios/login")
def listar_furgones(request):
    furgones = Furgon.objects.all()
    return render(request, 'furgones/listar_furgones.html', {'furgones': furgones})


@login_required(login_url="/usuarios/login")
def editar_furgon(request, pk):
    furgon = get_object_or_404(Furgon, pk=pk)
    if request.method == 'POST':
        form = FurgonForm(request.POST, instance=furgon)
        if form.is_valid():
            form.save()
            messages.success(request, 'Furgón actualizado exitosamente.')
            return redirect('furgones:listar_furgones')
    else:
        form = FurgonForm(instance=furgon)
    return render(request, 'furgones/editar_furgon.html', {'form': form, 'furgon': furgon})


@login_required(login_url="/usuarios/login")
def eliminar_furgon(request, pk):
    furgon = get_object_or_404(Furgon, pk=pk)
    if request.method == 'POST':
        furgon.delete()
        messages.success(request, 'Furgón eliminado exitosamente.')
        return redirect('furgones:listar_furgones')
    return render(request, 'furgones/eliminar_furgon.html', {'furgon': furgon})
