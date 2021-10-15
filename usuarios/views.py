#from rest_framework.views import APIView
#from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .serializers import UsuariosSerializer, UsuarioPutSerializer, UsuarioAutentificacion
from .models import Usuario
from .forms import FormularioRegistro, FormularioCambioCLave

# Envío de correo
def enviar_correo_registro(datosCorreo):
    print("pasando x aqui")
    return send_mail(
        'LinKraken',
        'Usuario creado sastifactoriamente. Bienvenido %s' % datosCorreo["usuario"],
        'cetr.newsletter@gmail.com',
        ['%s' % datosCorreo["email"]],
        fail_silently=False,
        )

def enviar_correo_recuperar_clave(datosCorreo):
    user = datosCorreo['usuario']
    token = datosCorreo['token']
    return send_mail(
        'LinKraken',
        "Hola %s de click al enlace para poder cambiar su contraseña http://localhost:8000/usuarios/cambioClave/?token=%s&usuario=%s" %(user,token,user),
        'cetr.newsletter@gmail.com',
        ['%s' % datosCorreo["email"]],
        fail_silently=False,
        )

#@login_required(login_url='/') 
def usuario_registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html')

    if request.method == 'POST':
        contra = make_password(request.POST['password'])
        model = Usuario()
        model.email = request.POST['email']
        model.password = contra
        model.usuario = request.POST['usuario']
        model.primer_nombre = request.POST['primer_nombre']
        model.primer_apellido = request.POST['primer_apellido']
        model.ci = request.POST['ci']
        model.save()
        messages.add_message(request, messages.SUCCESS, 'Registrado sastifactoriamente. Por favor revise su correo electronico para confirmar su cuenta.')
        # datosCorreo = {"usuario": request.POST['usuario'], "email": request.POST['email']}
        # enviar_correo_registro(datosCorreo)
        return HttpResponseRedirect("/")

def usuario_autentificacion(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return HttpResponseRedirect("/diligencias/")

    if request.method == 'POST':
        try:
            usuario = authenticate(email=request.POST['email'], password=request.POST['password'])
            print(usuario)
            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect("/diligencias/")
            messages.add_message(request, messages.ERROR, 'Correo o contraseña erronea. Por favor, verifique.')
            return HttpResponseRedirect("/")
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Correo o contraseña erronea. Por favor, verifique.')
            return HttpResponseRedirect("/")
        


def usuario_cambio_clave(request):
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.get(usuario=request.GET['usuario'])
            checkeo = PasswordResetTokenGenerator()
            is_valid = checkeo.check_token(usuario, request.GET['token'])
            if is_valid:
                return render(request, 'cambio_clave.html',{"usuario":usuario})
            else:
                messages.add_message(request, messages.ERROR, 'Enlace no coincide con el usuario')
                return HttpResponseRedirect("/usuarios")
            return HttpResponseRedirect("/usuarios")

        except Exception as identifier:
            messages.add_message(request, messages.ERROR, 'Problema con la Url')
            return HttpResponseRedirect("/usuarios")

        
def usuario_guardar_clave(request, pk):
    if request.method == 'POST':
        print(request.POST['password'])
        print(pk)
        contra = make_password(request.POST['password'])
        print(contra)
        model = Usuario.objects.get(pk=pk)
        model.password = contra
        model.save()
        messages.add_message(request, messages.SUCCESS, 'Su contraseña ha sido cambiada')
        return HttpResponseRedirect("/usuarios")
    return HttpResponseRedirect("/usuarios/cambioClave")

def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def usuario_recuperar_clave(request):
    if request.method == 'GET':
        return render(request, 'recuperar_password.html')
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(email=request.POST['email'])
            token_generador = PasswordResetTokenGenerator()
            token = token_generador.make_token(usuario)
            print(token)
            datosCorreo = {"token":token, "email":usuario.email, "usuario":usuario.usuario}
            enviar_correo_recuperar_clave(datosCorreo)
            messages.add_message(request, messages.SUCCESS, 'Revise su correo electronico')
            return HttpResponseRedirect("/usuarios") 
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Correo no existe')
            return HttpResponseRedirect("/usuarios/recuperarPassword") 

@login_required(login_url='/')        
def usuario_perfil(request):
    try:
        articulos = Articulos.objects.filter(usuario_id=request.user.id).order_by('-creacion_articulo')
        return render(request, "perfil.html", {"articulos":articulos})
    except Exception as e:
        print("ERROR: %s"%e)
        return HttpResponseRedirect("/") 

    



# ------------------------------------------ API VIEWS ------------------------------------------ #
# class Usuarios(APIView):

# # Obetener los datos solicitados en el modelo Usuario
#     def get_object(self, pk):
#         try:
#             return Usuario.objects.get(pk=pk)
#         except Usuario.DoesNotExist:
#             raise Http404



#     def get_ip(self,request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#            ip = x_forwarded_for.split(',')[0]
#            print(ip)
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#             print(ip)
#             return ip

# # Listar Usuarios (Solo desarrollo)
#     def get(self,request):
#         usuario = Usuario.objects.all()
#         serializer = UsuariosSerializer(usuario, many=True)
#         self.get_ip(request)
#         return Response(serializer.data)

# # Registro de Usuarios
#     def post(self, request):
#         password = make_password(request.data['password'])
#         request.data['password'] = password
#         datosCorreo = {"usuario": request.data['usuario'], "email": request.data['email']}
#         serializer = UsuariosSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             self.enviar_correo(datosCorreo)
#             return Response(serializer.data)
#         return Response(serializer.errors)

# # Cambio de Contraseña
#     def put(self, request, pk, format=None):
#         usuario = self.get_object(pk)
#         request.data['password'] = make_password(request.data['password'])
#         serializer = UsuarioPutSerializer(usuario, data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class Autentificacion(APIView):
#     def post(self, request):
#         user = authenticate(email=request.data['email'], password=request.data['password'])
#         usuario = Usuario.objects.get(email=user)
#         print(usuario)
#         serializer = UsuarioAutentificacion(usuario, data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             token_generar = PasswordResetTokenGenerator()
#             token = token_generar.make_token(usuario)
#             return Response({'token':token, 'usuario':serializer.data['email']})
#         else:
#             return Response("Te falta calle %s" % serializer.data)


