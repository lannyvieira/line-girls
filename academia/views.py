from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroAlunaForm, MatriculaForm
from .models import Matricula
from django.contrib import messages
from .models import Foto


def home(request):
    return render(request, 'academia/home.html')

def sobre(request):
    return render(request, 'academia/sobre.html')

def porque(request):
    return render(request, 'academia/porque.html')

def registrar_aluna(request):
    if request.method == 'POST':
        form = RegistroAlunaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('matricula')
    else:
        form = RegistroAlunaForm()
    return render(request, 'academia/registrar.html', {'form': form})

@login_required
def matricula(request):
    print("Entrou na view de matrícula")  # debug

    try:
        Matricula.objects.get(user=request.user)
        print("Usuário já possui matrícula")
        return redirect('dashboard')
    except Matricula.DoesNotExist:
        print("Usuário ainda não possui matrícula")

    if request.method == 'POST':
        print("Recebido POST com dados:", request.POST)
        form = MatriculaForm(request.POST)
        if form.is_valid():
            print("Formulário válido")
            matricula = form.save(commit=False)
            matricula.user = request.user
            matricula.save()
            return redirect('dashboard')
        else:
            print("Formulário inválido:", form.errors)
    
    else:
        form = MatriculaForm()
    
    return render(request, 'academia/matricula.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
        
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'academia/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    matricula = Matricula.objects.get(user=request.user)
    return render(request, 'academia/dashboard.html', {'matricula': matricula})

@login_required
def editar_matricula(request):
    matricula = get_object_or_404(Matricula, user=request.user)

    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MatriculaForm(instance=matricula)

    return render(request, 'academia/editar_matricula.html', {'form': form})


def landing_page(request):
    return render(request, 'academia/landing.html')


def galeria(request):
    fotos_academia = Foto.objects.filter(categoria='academia')
    fotos_eventos = Foto.objects.filter(categoria='eventos')
    return render(request, 'academia/galeria.html', {
        'fotos_academia': fotos_academia,
        'fotos_eventos': fotos_eventos
    })
