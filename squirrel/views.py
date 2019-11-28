from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
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


def update(request,squirrel_uni):
    squirrel = get_object_or_404(Squirrel,Uni=squirrel_uni)
    return render(request, 'squirrel/detail.html',{'squirrel':squirrel})

def kk(request,squirrel_uni):
    squirrel = get_object_or_404(Squirrel,Uni=squirrel_uni)
    squirrel.Lat = request.POST.get('Lat',False)
    return HttpResponse('kk')
