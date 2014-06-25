from django.conf.urls import patterns,url 

urlpatterns=patterns('sysadt.webservices.wsProductos.views',
	url(r'^ws/productos/$','wsProductos_view',name= "wsproducto"),

	)