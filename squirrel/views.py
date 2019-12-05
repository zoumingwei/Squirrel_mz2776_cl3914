from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Squirrel
from django.template import loader
from .forms import SquirrelForm
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
    squirrel = get_object_or_404(Squirrel, Uni=squirrel_uni)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance=squirrel)

        if form.is_valid():
            form.save()
            return HttpResponse('kk')
        
    else:
        form = SquirrelForm(instance=squirrel)

    context = {'form':form}

    return render(request, 'squirrel/update.html',context)

def add(request):
    print('000')
    return HttpResponse('Squirrel!')



def stats(request):
    return HttpResponse('Squirrel Stats!')
