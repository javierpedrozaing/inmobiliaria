from django.conf.urls import patterns, url
from inmuebles.views import inmueblesListView, inmuebleDetailView
from .models import Inmuebles

urlpatterns = patterns('',
	url(r'^inmuebles/(?P<titulo>[\w\-\W]+)/$', inmuebleDetailView.as_view(), name='inmueble_detail'),
)
