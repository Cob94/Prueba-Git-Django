
from django.conf.urls import patterns, include, url
urlpatterns=patterns('home.views',
	url(r'^$', 'index_view', name='principal'),
	url(r'^hacerca/$', 'about_view', name='Hacerca de'),
	url(r'^productos/page/(?P<pagina>.*)/$','productos_views',name='vista_productos'),
	url(r'^contacto/$', 'contacto_view', name='Vista contactanos'),
	url(r'^login/$', 'login_view', name='Vista Login'),
	url(r'^logout/$', 'logout_view', name='Vista Logout'),
	url(r'^producto/(?P<id_prod>\d+)/$', 'singleProducto_views', name='Vista un producto'),
	)