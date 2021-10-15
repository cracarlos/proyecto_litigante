from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('diligencia_crear', views.diligencia_crear, name='diligencia_crear'),
    path('diligencia_detalles/<int:id>', views.diligencia_detalles, name='diligencia_detalles'),
    path('diligencia_editar/<int:id>', views.diligencia_editar, name='diligencia_editar'),
]
