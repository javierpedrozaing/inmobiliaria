from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, RedirectView, ListView, DetailView
from .models import Inmuebles

# Create your views here.
class JsonResponseMixin(object):

    def response_handler(self):
        format = self.request.GET.get('format', None)
        if format == 'json':
            return self.json_to_response()

        context = self.get_context_data()
        return self.render_to_response(context)

    def json_to_response(self):
        data = self.get_data()
        return JsonResponse(data, safe=False)



#class inmueblesView(TemplateView):

#	template_name = 'inmuebles.html'


#class inmueblesRedirectView(RedirectView):
#	pattern_name = 'inmuebles'


class inmueblesListView(JsonResponseMixin, ListView):
	model = Inmuebles
	template_name = 'inmuebles.html'
	paginate_by = 2

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		return self.response_handler()

	def get_context_data(self, **kwargs):
		context = super(inmueblesListView, self).get_context_data(**kwargs)
		page = self.request.GET.get('page')
		context.update({'page': page})
		return context

	def get_data(self):
		data = [{
            'logo': inmueble.logo.url,
            'title': inmueble.titulo,
        } for inmueble in self.object_list]

		return data

	def get_queryset(self):
		if self.kwargs.get('inmueble'):
			queryset = self.model.objects.filter(inmueble__slug__contains=self.keargs['inmueble'])
		else:
			queryset = super(inmueblesListView, self).get_queryset()

		return queryset

class inmuebleDetailView(JsonResponseMixin, DetailView):
	model = Inmuebles
	template_name = 'inmueble_detalle.html'
	slug_url_kwarg = 'titulo'
	slug_field = 'titulo'

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		return self.response_handler()

	def get_data(self):
		data = {
			'inmuebles': {
				'titulo': self.object.titulo,			
			}
		}
		return data
