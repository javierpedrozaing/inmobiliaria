from django.shortcuts import render, render_to_response,get_object_or_404
from inmuebles.models import Inmuebles
# Create your views here.

def home(request):
	inmuebles = Inmuebles.objects.all()
	return render_to_response('index.html')

