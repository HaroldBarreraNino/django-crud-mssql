from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Cifra_Clave
from .forms import CifraClaveForm

# Create your views here.
def principal(request):
    return render(request, 'principal.html')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': '¡Nombre de usuario o contraseña incorrectos!'
            })
        else:
            login(request, user)
            return redirect('cifras_claves')


def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cifras_claves')
            except IntegrityError:
                return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    'error': '¡Este usuario ya existe!'
                })
        else:
            return render(request, 'registrarse.html', {
                'form': UserCreationForm,
                'error': '¡Las contraseñas no coinciden!'
            })


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('principal')

@login_required
def cifras_claves(request):
    query = request.GET.get('q')
    Area = request.GET.get('Area')
    cifras = Cifra_Clave.objects.all()
    
    #Filtros y barra de busqueda
    if query:
        cifras = cifras.filter(titulo__icontains=query)

    if Area:
        cifras = cifras.filter(Area=Area)

    return render(request, 'cifras_claves.html',{
        'cifras': cifras
    })

@login_required
def crear_cifra_clave(request):
    if request.method == 'GET':
        return render(request, 'crear_cifra_clave.html', {
            'form': CifraClaveForm
        })
    else:
        try:
            form = CifraClaveForm(request.POST)
            new_cifra = form.save(commit=False)
            new_cifra.usuario = request.user
            new_cifra.save()
            return redirect('cifras_claves')
        except ValueError:
            return render(request, 'crear_cifra_clave.html', {
                'form': CifraClaveForm,
                'error': 'Porfavor, ingresa valores validos'
            })