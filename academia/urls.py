from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('porque/', views.porque, name='porque'),
    path('registrar/', views.registrar_aluna, name='registrar'),
    path('matricula/', views.matricula, name='matricula'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar-matricula/', views.editar_matricula, name='editar_matricula'),
    path('promo/', views.landing_page, name='landing'),
    path('galeria/', views.galeria, name='galeria')

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

