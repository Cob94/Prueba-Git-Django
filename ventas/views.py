# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from ventas.forms import addProductForm
from ventas.models import Producto
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def add_product_view(request):
	info = "Inicializando" 
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen'] # Esto se obtiene con el request.FILES
				precio = form.cleaned_data['precio']
				stock = form.cleaned_data['stock']
				p = Producto()
				if imagen: # Generamos una pequenia validacion.
					p.imagen = imagen
				p.nombre 		=  nombre
				p.descripcion 	= descripcion
				p.precio 		= precio
				p.stock 		= stock
				p.status = True
				p.save() # Guardar la informacion
				info = "Se guardo satisfactoriamente!!!!!"
			else:
				info = "informacion con datos incorrectos"			
		form = addProductForm()
		ctx = {'form':form, 'informacion':info}
		return render_to_response('ventas/addproducto.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
def edit_prod_view(request,id_prod):
	p=Producto.objects.get(id=id_prod)
	if request.method =="GET":
		form= addProductForm(initial={
			'nombre':p.nombre,
			'descripcion':p.descripcion,
			'precio':p.precio,
			'stock':p.stock,
			})
	ctx={'form':form,'producto':p}
	return render_to_response('ventas/edit_producto.html',ctx,context_instance=RequestContext(request))



"""
def add_producto_view(request):
	if request.method=="POST":
		form=addProductoForm(request.POST,request.FILES)
		info="Inicializando"
		if form.is_valid():
			nombre=form.cleaned_data['nombre']
			descripcion=form.cleaned_data['descripcion']
			imagen=forms.cleaned_data['imagen'] #ESto se obitiene con el Request.FILES
			precio=forms.cleaned_data['precio']
			stock=forms.cleaned_data['stock']

			p=Producto()
			if imagen: #Generamos la validacion si el usuraio sube una imagen..
				p.imagen=imagen
			p.nombre=nombre
			p.descripcion= descripcion
			p.status= True
			p.precio=precio
			p.stock=stock
			p.save()
			info="Se guardo Satisfactoriamente"
		else:
			info="Informacion con datos incorrectos"
		form= addProductoForm()
		ctx={'form':form,'Informacion':info}
		return render_to_response('ventas/addproducto.html',ctx, context_instance=RequestContext(request))
	else:
		form= addProductoForm()
		ctx={'form':form}
		return render_to_response('ventas/addproducto.html',ctx, context_instance=RequestContext(request))
"""