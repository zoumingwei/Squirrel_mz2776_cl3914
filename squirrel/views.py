from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Squirrel
from django.template import loader
# Create your views here.


def test(request):
    return HttpResponse('Catastrophic Squirrels')

def sighting(request):
    all_squirrels = Squirrel.objects.all()
    template = loader.get_template('squirrel/sighting.html')
    context = {
            'all_squirrels':all_squirrels,
    }
    
    return HttpResponse(template.render(context,request))
