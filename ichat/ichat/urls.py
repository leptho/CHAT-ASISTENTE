"""ichat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))


from django.conf.urls import url, patterns, include
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^preguntas/', views.index, name='preguntas'),
    url(r'^preguntas/crear/$',views.pregunta_crear, name="pregunta_crear"),
    url(r'^preguntas/(?P<pregunta_id>\d+)/$', views.pregunta_detalle, name='pregunta_detalle'),
    url(r'^preguntas/editar/(?P<pregunta_id>\d+)/$',views.pregunta_editar, name='pregunta_editar'),
]
"""

from bot import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from preguntas import views
from django.core.urlresolvers import reverse

urlpatterns = patterns('',    
    url(r'^$', 'bot.views.bot', name='bot'),
    url(r'^entrenar/', 'bot.views.entrenar', name='entrenar'),
    url(r'^pregunta_borrar/(?P<pregunta_id>\d+)/$', 'preguntas.views.pregunta_borrar', name='pregunta_borrar'),
    url(r'^preguntas/$', 'preguntas.views.index', name='preguntas'),
    url(r'^preguntas/(?P<pregunta_id>\d+)/$', 'preguntas.views.pregunta_detalle', name='pregunta_detalle'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^preguntas/crear/$','preguntas.views.pregunta_crear',name="pregunta_crear"),
    url(r'^preguntas/editar/(?P<pregunta_id>\d+)/$','preguntas.views.pregunta_editar', name='pregunta_editar'),
    url(r'^obtenersalida', 'bot.views.obtenersalida', name='obtenersalida')
)
