from django.conf.urls import patterns,url 

urlpatterns=patterns('ventas.views',
	url(r'^add/producto/$','add_product_view',name= "vista_agregar_producto"),
	url(r'^edit/producto/(?P<id_prod>.*)/$','edit_prod_view',name= "vista_editar_producto"),
	)