from django import forms
from .models import Matricula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroAlunaForm(UserCreationForm):
    first_name = forms.CharField(label='Nome completo')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        help_texts = {field: '' for field in fields}
        
class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['cpf', 'telefone', 'plano']
        labels = {
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'plano': 'Plano escolhido'
        }
