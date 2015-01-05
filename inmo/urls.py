from django.conf.urls import patterns, include, url
from django.contrib import admin
from inmuebles.views import inmueblesListView, inmuebleDetailView
from django.views.generic import TemplateView, RedirectView



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'inmobiliaria.views.home', name='home'),
  	# url(r'^inmuebles/$', inmueblesView.as_view(), name='inmuebles.html'),
  	url(r'^inmuebles/$', inmueblesListView.as_view(), name='inmuebles_list'),
  	#url(r'^inmuebles/(?P<inmueble>[\W\]-]+)/$', inmueblesListView.as_view(), name='inmueble_list'),
  	url(r'', include('inmuebles.urls')),

  	#url(r'^casas/$', RedirectView.as_view(permanent= False, url= '/inmuebles/'), name='inmuebles'),
  	#url(r'^casas/$', inmueblesRedirectView.as_view(), name='casas'),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
