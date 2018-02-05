from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Pregunta(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.pregunta

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.respuesta_corta = 'Preguntado hoy'
        
'''
class Respuesta(models.Model):
    Pregunta = models.ForeignKey(Pregunta)
    contenido = models.TextField()
    mejor_respuesta = models.BooleanField("Respuesta preferida", default=False)

    def _str_(self):
        return self.contenido
'''
