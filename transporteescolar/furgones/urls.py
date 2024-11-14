from django.urls import path
from . import views

app_name = "furgones"

urlpatterns = [
    path('registrar_furgon/', views.registrar_furgon, name='registrar_furgon'),
    path('', views.listar_furgones, name='listar_furgones'),
    path('editar_furgon/<int:pk>/', views.editar_furgon, name='editar_furgon'),
    path('eliminar_furgon/<int:pk>/',
         views.eliminar_furgon, name='eliminar_furgon'),
]
