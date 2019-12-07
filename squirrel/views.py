from django.shortcuts import render, get_object_or_404
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
            'all_squirrels': all_squirrels,
    }
    
    return HttpResponse(template.render(context, request))


def update(request,squirrel_uni):
    squirrel = get_object_or_404(Squirrel, Uni=squirrel_uni)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks for keeping an eye on them. Squirrels are dangerous!')
    else:
        form = SquirrelForm(instance=squirrel)
    context = {'form': form}

    return render(request, 'squirrel/update.html', context)

def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks for reporting them. Squirrels are dangerous!')
    else:
        form = SquirrelForm()
    context = {'form': form}

    return render(request, 'squirrel/update.html', context)


def stats(request):
    from django.db.models import Count
    import datetime
    AM_squirrel = Squirrel.objects.filter(Shift='AM').count()
    PM_squirrel = Squirrel.objects.filter(Shift='PM').count()
    
    approaching_squirrel = Squirrel.objects.filter(Approaches=True).count()
    
    adult_squirrel = Squirrel.objects.filter(Age='Adult').count()
    young_squirrel = Squirrel.objects.filter(Age='Juvenile').count()

    recent = Squirrel.objects.filter(Date__gt=datetime.date(2019, 1, 1)).count()
   
    on_ground = Squirrel.objects.filter(Location='Ground Plane').count()
    above_ground = Squirrel.objects.filter(Location='Above Ground').count()
   
    context = {
            'AM_squirrel': AM_squirrel,
            'PM_squirrel': PM_squirrel,
            'approaching_squirrel': approaching_squirrel,
            'adult_squirrel': adult_squirrel,
            'young_squirrel': young_squirrel,
            'recent': recent,
            'on_ground': on_ground,
            'above_ground': above_ground,
            }
    return render(request, 'squirrel/stats.html', context)


def map(request):
    sightings = Squirrel.objects.all()
    context = {
            'sightings':sightings,
    }
    return render(request, 'squirrel/map.html', context)
