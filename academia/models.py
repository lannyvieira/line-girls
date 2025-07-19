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

class Horario(models.Model):
    atividade = models.CharField(max_length=100)
    dia_semana = models.CharField(max_length=10, choices=[
        ('segunda', 'Segunda'),
        ('terca', 'Terça'),
        ('quarta', 'Quarta'),
        ('quinta', 'Quinta'),
        ('sexta', 'Sexta'),
        ('sabado', 'Sábado')
    ])
    horario = models.TimeField()

    def __str__(self):
        return f"{self.atividade} - {self.dia_semana.title()} às {self.horario.strftime('%H:%M')}"

class PersonalTrainer(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to='personals/', blank=True, null=True)
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    

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
