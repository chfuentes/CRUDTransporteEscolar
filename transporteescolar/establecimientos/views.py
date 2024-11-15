from django.shortcuts import render, redirect, get_object_or_404
from .models import Establecimiento
from .forms import EstablecimientoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url="/usuarios/login")
@user_passes_test(lambda u: u.is_superuser)
def registrar_establecimiento(request):
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Establecimiento registrado exitosamente.')
            return redirect('establecimientos:listar_establecimientos')
    else:
        form = EstablecimientoForm()
    return render(request, 'establecimientos/registrar_establecimiento.html', {'form': form})


@login_required(login_url="/usuarios/login")
def listar_establecimientos(request):
    establecimientos = Establecimiento.objects.all()
    return render(request, 'establecimientos/listar_establecimientos.html', {'establecimientos': establecimientos})


@login_required(login_url="/usuarios/login")
@user_passes_test(lambda u: u.is_superuser)
def editar_establecimiento(request, id):
    establecimiento = get_object_or_404(Establecimiento, id=id)
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST, instance=establecimiento)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Establecimiento actualizado exitosamente.')
            return redirect('establecimientos:listar_establecimientos')
    else:
        form = EstablecimientoForm(instance=establecimiento)
    return render(request, 'establecimientos/editar_establecimiento.html', {'form': form, 'establecimiento': establecimiento})


@login_required(login_url="/usuarios/login")
@user_passes_test(lambda u: u.is_superuser)
def eliminar_establecimiento(request, id):
    establecimiento = get_object_or_404(Establecimiento, id=id)
    if request.method == 'POST':
        establecimiento.delete()
        messages.success(request, 'Establecimiento eliminado exitosamente.')
        return redirect('establecimientos:listar_establecimientos')
    return render(request, 'establecimientos/eliminar_establecimiento.html', {'establecimiento': establecimiento})
