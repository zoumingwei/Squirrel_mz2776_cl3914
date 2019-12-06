from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('map',views.map,name='map'),
    path('sightings',views.sighting,name='sighting'),
    path('sightings/add',views.add,name='add'),
    path('sightings/stats',views.stats,name='stats'),
    path('sightings/<squirrel_uni>',views.update,name='update'),
]
