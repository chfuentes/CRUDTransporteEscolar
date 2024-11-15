from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@login_required(login_url="/usuarios/login")
@user_passes_test(lambda u: u.is_superuser)
def registro(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = form.cleaned_data.get('is_staff')
            user.is_superuser = form.cleaned_data.get('is_superuser')
            user.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('/')
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {username}!')
                if 'next' in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect('/')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


@login_required
def logout_view(request):
    usuario = request.user
    logout(request)
    messages.success(request,  f"El usuario {usuario} cerró sesión")
    return redirect('/')


@login_required
def perfil(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(
            user=request.user, data=request.POST)
        if profile_form.is_valid():
            profile_form.save()
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Datos actualizados')
            return redirect('usuarios:perfil')
    else:
        profile_form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
    return render(request, 'usuarios/perfil.html', {
        'profile_form': profile_form,
        'password_form': password_form
    })
