from django.shortcuts import render
from .models import Mensaje

def mensajes_recibidos(request):

    # Filtra los mensajes recibidos por el destinatario
    mensajes = Mensaje.objects.filter(destinatario='Sabrina')

    # Pasa los mensajes a la plantilla
    return render(request, 'recibidos.html', {'mensajes': mensajes})