from django.contrib import admin
from .models import Matricula, Horario, PersonalTrainer
from .models import FotoGaleria
from .models import Foto

admin.site.register(Matricula)
admin.site.register(Horario)
admin.site.register(PersonalTrainer)
admin.site.register(FotoGaleria)
admin.site.register(Foto)
