from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('sightings',views.sighting,name='sighting'),
    path('<squirrel_uni>',views.update,name='update'),
    path('<squirrel_uni>/kk/',views.kk,name='kk'),
]
