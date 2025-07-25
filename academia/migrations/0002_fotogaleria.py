# Generated by Django 5.2.4 on 2025-07-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoGaleria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100)),
                ('imagem', models.ImageField(upload_to='galeria/')),
                ('descricao', models.TextField(blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
