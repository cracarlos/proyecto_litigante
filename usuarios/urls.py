from django.urls import path
from . import views


urlpatterns = [
    path('', views.usuario_autentificacion, name='login'),
    path('registro/', views.usuario_registro, name='registro'),
    path('cambioClave/', views.usuario_cambio_clave),
    path('cambioClave/<slug:token>/<str:usuario>', views.usuario_cambio_clave),
    path('cambioClave/<int:pk>', views.usuario_guardar_clave),
    path('recuperarPassword/', views.usuario_recuperar_clave, name = 'recuperarPassword'),
    path('logout/', views.usuario_logout, name='logout'),
    path('perfil/', views.usuario_perfil, name='perfil'),
    # path('api/', views.Usuarios.as_view()),
    # path('api/<int:pk>', views.Usuarios.as_view()),
    # path('api/auth', views.Autentificacion.as_view()),
]
