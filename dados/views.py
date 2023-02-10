from django.shortcuts import render
from .models import Gato
# Create your views here.

def index(request):
    context = {
        'Gato': Gato.objects.order_by('nome'),
    }
    return render(request,'index.html', context)