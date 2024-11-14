from django.urls import path
from . import views

app_name = "establecimientos"
urlpatterns = [
    path('registrar_establecimiento/', views.registrar_establecimiento,
         name='registrar_establecimiento'),
    path('', views.listar_establecimientos, name='listar_establecimientos'),
    path('editar_establecimiento/<int:id>/',
         views.editar_establecimiento, name='editar_establecimiento'),
    path('eliminar_establecimiento/<int:id>/',
         views.eliminar_establecimiento, name='eliminar_establecimiento'),
]
