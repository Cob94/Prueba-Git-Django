# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from ventas.models import Producto
from home.forms import ContactoForm, loginform
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator ,EmptyPage,InvalidPage

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))
def about_view(request):
	mensaje="Esto es un mensaje desde mi lista"
	ctx={'msg':mensaje}
	return render_to_response('home/about.html',ctx, context_instance=RequestContext(request))

def productos_views(request,pagina):
	lista_prod = Producto.objects.filter(status=True) # Select * from ventas_productos where status = True
	paginator = Paginator(lista_prod,5) # Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)
	ctx = {'productos':productos}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def singleProducto_views(request,id_prod):
	prod=Producto.objects.get(id=id_prod)
	ctx={'producto':prod}
	return render_to_response('home/singleprod.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado=False
	email=""
	titulo=""
	texto=""
	if request.method=="POST": #Definir si se envio la informacion o no se envio
		formulario=ContactoForm(request.POST) #llenar la el form con la info del POST
		if formulario.is_valid():
			info_enviado=True
			email=formulario.cleaned_data['Email']
			titulo= formulario.cleaned_data['Titulo']
			texto=formulario.cleaned_data['Texto']

	else:
		formulario=ContactoForm()
	ctx={'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx, context_instance=RequestContext(request))

def login_view(request):
	mensaje=""

	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method=="POST":
			form= loginform(request.POST)
			if form.is_valid():
				username= form.cleaned_data['username']
				password=form.cleaned_data['password']
				usuario=authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje="Usuario y/o Password Incorrectos"
		form=loginform()
		ctx={'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
	