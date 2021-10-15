from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required

from diligencias.models import Diligencias

import qrcode
from itsdangerous import URLSafeSerializer

@login_required(login_url='/') 
def index(request):
    print("Listado de diligencias")
    listado = Diligencias.objects.all()
    return render(request, 'diligencias/index.html', {'listado': listado})

@login_required(login_url='/') 
def diligencia_crear(request):
    if request.method == 'GET':
        try:
            print("Entrando en deligencia_crear")
            return render(request, 'diligencias/deligencia_crear.html')
            
        except Exception as e:
            print(f"ERROR: {e}")
            messages.add_message(request, messages.ERROR, 'Error al guardar')
            return HttpResponseRedirect("/diligencias/deligencia_crear")

    if request.method == 'POST':
        try:
            print("Guardando en deligencia_crear")
            model = Diligencias()
            model.cliente = request.POST['cliente']
            model.ci = request.POST['ci']
            model.fecha = request.POST['fecha']
            model.cualidad = request.POST['cualidad']
            model.contraparte = request.POST['contraparte']
            model.k = request.POST['k']
            model.or_policial = request.POST['or_policial']
            model.direccion_reclusion = request.POST['direccion_reclusion']
            model.juzgado = request.POST['juzgado']
            model.secretario = request.POST['secretario']
            model.fiscalia = request.POST['fiscalia']
            model.ubicacion = request.POST['ubicacion']
            model.fiscal = request.POST['fiscal']
            model.mp = request.POST['mp']
            model.pronunciamiento = request.POST['pronunciamiento']
            model.sala = request.POST['sala']
            model.ejecucion = request.POST['ejecucion']
            model.amparo = request.POST['amparo']
            model.casacion = request.POST['casacion']
            model.delitos = request.POST['delitos']
            model.juez = request.POST['juez']
            model.save()

            messages.add_message(request, messages.SUCCESS, 'Guardado')
            return HttpResponseRedirect("/diligencias/")
            
        except Exception as e:
            print(f"ERROR: {e}")
            messages.add_message(request, messages.ERROR, 'Error al guardar')
            return HttpResponseRedirect("/diligencias/deligencia_crear")

def diligencia_detalles(request, id):
    if request.method == 'GET':
        try:
            print("Entrando en deligencia_detalles")
            diligencia = Diligencias.objects.get(id = id)
            # Token
            auth_s = URLSafeSerializer("django-insecure-#yl0s_bzm)4&bo%xkv1&!g%*)urojb83bo4!(udp57fy*m(xd#")
            token = auth_s.dumps({"id": id})
            print(token)
            # QR consulta
            img = qrcode.make(f"http://localhost:8000/deligencia_detalles/{id}")
            f = open(f"./diligencias/static/diligencias/img/qr/{id}.png", "wb")
            img.save(f)
            f.close()

            # QR detalles
            img = qrcode.make(
            f"""
            Cliente:
            {diligencia.cliente}
            
            Cédula:
            {diligencia.ci}

            Fecha:
            {diligencia.fecha}

            Cualidad:
            {diligencia.cualidad}

            Delitos:
            {diligencia.delitos}

            Contraparte:
            {diligencia.contraparte}
            
            K:
            {diligencia.k}

            Org. Policial:
            {diligencia.or_policial}

            Dirección Reclusión:
            {diligencia.direccion_reclusion}

            Juzgado:
            {diligencia.juzgado}
            
            Secretario (a):
            {diligencia.secretario}

            Fiscalia:
            {diligencia.fiscalia}

            Ubicación:
            {diligencia.ubicacion}

            Fiscal:
            {diligencia.fiscal}

            MP:
            {diligencia.mp}

            Causa:
            {diligencia.causa}

            Pronunciamiento:
            {diligencia.pronunciamiento}

            Sala:
            {diligencia.sala}

            Decisión:
            {diligencia.decision}

            Ejecución:
            {diligencia.ejecucion}

            Amparo:
            {diligencia.amparo}

            Casación:
            {diligencia.casacion}

            
             """)
            f = open(f"./diligencias/static/diligencias/img/qr/{id}_detalles.png", "wb")
            img.save(f)
            f.close()
            return render(request, 'diligencias/deligencia_detalles.html' , {'diligencia': diligencia})
            
        except Exception as e:
            print(f"ERROR: {e}")
            messages.add_message(request, messages.ERROR, 'Error al ver los detalles')
            return HttpResponseRedirect("/")


@login_required(login_url='/') 
def diligencia_editar(request, id):
    if request.method == 'GET':
        try:
            print("Entrando en deligencia_editar")
            diligencia = Diligencias.objects.get(id = id)
            return render(request, 'diligencias/deligencia_editar.html', {'diligencia': diligencia})
            
        except Exception as e:
            print(f"ERROR: {e}")
            messages.add_message(request, messages.ERROR, 'Error al guardar')
            return HttpResponseRedirect("/diligencias/deligencia_crear")

    if request.method == 'POST':
        try:
            print("Guardando en deligencia_editar")
            model = Diligencias.objects.get(id = id)
            model.cliente = request.POST['cliente']
            model.ci = request.POST['ci']
            model.fecha = request.POST['fecha']
            model.cualidad = request.POST['cualidad']
            model.contraparte = request.POST['contraparte']
            model.k = request.POST['k']
            model.or_policial = request.POST['or_policial']
            model.direccion_reclusion = request.POST['direccion_reclusion']
            model.juzgado = request.POST['juzgado']
            model.secretario = request.POST['secretario']
            model.fiscalia = request.POST['fiscalia']
            model.ubicacion = request.POST['ubicacion']
            model.fiscal = request.POST['fiscal']
            model.mp = request.POST['mp']
            model.pronunciamiento = request.POST['pronunciamiento']
            model.sala = request.POST['sala']
            model.ejecucion = request.POST['ejecucion']
            model.amparo = request.POST['amparo']
            model.casacion = request.POST['casacion']
            model.delitos = request.POST['delitos']
            model.causa = request.POST['causa']
            model.decision = request.POST['decision']
            model.juez = request.POST['juez']
            model.save()

            messages.add_message(request, messages.SUCCESS, 'Guardado')
            return HttpResponseRedirect("/diligencias/")
            
        except Exception as e:
            print(f"ERROR: {e}")
            messages.add_message(request, messages.ERROR, 'Error al guardar')
            return HttpResponseRedirect("/diligencias/")
