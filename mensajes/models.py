from django.db import models

class Mensaje(models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=200)
    destinatario = models.CharField(max_length=200)
    fecha_envio = models.DateTimeField()

    def __str__(self):
        return f'De {self.remitente} a {self.destinatario} - {self.texto[:20]}'