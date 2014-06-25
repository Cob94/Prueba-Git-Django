# Create your views here.
from django.http import HttpResponse
from ventas.models import Producto
from django.core import serializers
#INtegramos las serializadcion de los objetos

def wsProductos_view(request):
	data = serializers.serialize("json",Producto.objects.filter(status=True))
	#Retorna la INfo en formato Json
	return HttpResponse(data,mimetype='application/json')