from django.db import models
from django.contrib.auth.models import User

class Matricula(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    plano = models.CharField(max_length=100, choices=[
        ('mensal', 'Mensal'),
        ('trimestral', 'Trimestral'),
        ('anual', 'Anual')
    ])
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plano}"


CATEGORIAS = [
    ('academia', 'Academia'),
    ('eventos', 'Eventos'),
]

class Foto(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='galeria/')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
