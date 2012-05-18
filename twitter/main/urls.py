from django.conf.urls.defaults import patterns, include, url

#Puedes agregar entre las lineas patterns ('main.views'
#para evitar escribir la url completa
urlpatterns = patterns('',
    url(r'^$','main.views.home', name='home'),
    url(r'^user/add/$', 'main.views.add_User', name='add_User' ),
    url(r'^user/Register/$', 'main.views.User_Registration', name='User_Registration' ),
    url(r'^user/login/$', 'main.views.LoginRequest', name='LoginRequest' ),
    url(r'^user/logout/$', 'main.views.LogoutRequest', name='LogoutRequest' ),
    url(r'^user/sesion/$', 'main.views.sesion', name='sesion' ),
	url(r'^user/(?P<username>[a-zA-Z0-9\\_]+)/$', 'main.views.profile', name='profile'),
    url(r'^user/all/$', 'main.views.all', name='all' ),
    url(r'^user/userss/$', 'main.views.userss', name='userss' ),
    url(r'^user/sesion/edit$', 'main.views.edit_user', name='edit_user'),
)
	