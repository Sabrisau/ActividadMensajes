from django.shortcuts import render
from .models import Mensaje

def mensajes_recibidos(request):
    # Obtener el destinatario desde la solicitud 
    destinatario = request.user  # Suponiendo que el usuario actual es el destinatario

    # Filtra los mensajes recibidos por el destinatario
    mensajes = Mensaje.objects.filter(destinatario=destinatario)

    # Pasa los mensajes a la plantilla
    return render(request, 'mensajes/recibidos.html', {'mensajes': mensajes})