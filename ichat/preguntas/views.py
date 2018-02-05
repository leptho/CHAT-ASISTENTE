from django.http import HttpResponse, Http404
from preguntas.models import Pregunta
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect 
from django.template import RequestContext
from preguntas.form import PreguntaForm
from django.utils import timezone
from django.template import RequestContext

def index(request):
    preguntas = Pregunta.objects.all()
    return render_to_response('preguntas/index.html',
                                        {'preguntas': preguntas})    

def pregunta_detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render_to_response('preguntas/pregunta_detalle.html',
                                        {'pregunta':pregunta})

def pregunta_borrar(request, pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    pregunta.delete()
    preguntas = Pregunta.objects.all()
    return render_to_response('preguntas/borrada.html')

def pregunta_crear(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():          
            form.save()
            return redirect('preguntas')
    else:
        form = PreguntaForm()
    return render_to_response('preguntas/pregunta_crear.html',
                {'form':form},
                context_instance=RequestContext(request))
            

def pregunta_editar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    if request.method == 'POST':
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('pregunta_detalle', pregunta_id)
    else:
        form = PreguntaForm(instance=pregunta)
    return render_to_response('preguntas/pregunta_editar.html',
                                                {'form': form},
                    context_instance=RequestContext(request))
