from django.urls import path
from . import views

app_name = "choferes"

urlpatterns = [
    path('registrar_chofer/', views.registrar_chofer, name='registrar_chofer'),
    path('', views.listar_choferes, name='listar_choferes'),
    path('editar_chofer/<int:id>/', views.editar_chofer, name='editar_chofer'),
    path('eliminar_chofer/<int:id>/',
         views.eliminar_chofer, name='eliminar_chofer'),

]
