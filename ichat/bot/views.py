#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from preguntas.models import Pregunta
from django.template import RequestContext

import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
chatbot = ChatBot("Ron Obvious") 

def bot(request):
    return render_to_response('bot/index.html',RequestContext(request))

def obtenersalida(request):
    if request.is_ajax():
	if request.method == 'POST': 
			entrada2 = request.POST.get('texto_entrada')
			print ("Pregunta iChat: "+entrada2)
			salida2 = str(chatbot.get_response(entrada2))
			print ("Respuesta iChat: " +salida2) 
			return HttpResponse(salida2)


def entrenar(request):
    #subprocess.call('rm /home/leptho/Escritorio/CHAT\ ASISTENTE/ichat/database.db', shell=True)	
    cuerpo = []	
    preguntas = Pregunta.objects.all()
    for pregunta in preguntas:
	print(pregunta.pregunta)
	cuerpo.append(pregunta.pregunta)
	cuerpo.append(pregunta.respuesta)
    chatbot = ChatBot("Ron Obvious")
    chatbot.set_trainer(ListTrainer)
    chatbot.train(cuerpo)
    print("Se realizó el entrenamiento chat")
    return render_to_response('bot/entrenar.html',
                                        {'preguntas': preguntas})


