import datetime
from django.shortcuts import render
from django.http import Http404, HttpResponse

def hola(request):
	return HttpResponse("Hola mundo")

def fecha_actual(request):
	ahora = datetime.datetime.now()
	ctx = {'fecha_actual':ahora}
	return render(request,'fecha_actual.html', ctx)

def horas_adelante(request, horas):
	try:
		horas = int(horas)
	except ValueError:
		raise Http404();
	dt = datetime.datetime.now() + datetime.timedelta(hours=horas)
	ctx = {'hora_siguiente':dt, 'horas':horas}
	return render(request, 'horas_adelante.html', ctx)