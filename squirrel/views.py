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
            return HttpResponse('Thanks for keeping an eye on them. Squirrels are dangerous!')
        
    else:
        form = SquirrelForm(instance=squirrel)

    context = {'form':form}

    return render(request, 'squirrel/update.html',context)

def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Thanks for reporting them. Squirrels are dangerous!')
        
    else:
        form = SquirrelForm()

    context = {'form':form}

    return render(request, 'squirrel/update.html',context)


def stats(request):
    return HttpResponse('Squirrel Stats!')

def map(request):
    return HttpResponse('This is a map')
