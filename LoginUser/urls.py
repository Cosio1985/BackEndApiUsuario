from django.urls import path
from . import views # de esta forma importamos todas las vistas del archivo views.py de la app LoginUser

urlpatterns = [
    #estos paths son los endpoints de la API para registrar un usuario y obtener su perfil
    path('api/registro/', views.registrar_usuario, name='registrar_usuario'),
    path('api/perfil/', views.perfil_usuario, name='perfil_usuario'),
]
