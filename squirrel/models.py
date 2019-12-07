from django.db import models
from django.utils.translation import gettext as _



    
class Squirrel(models.Model):
    Lat = models.FloatField('Latitude', null=True)
    Long = models.FloatField('Longitude')
    Uni = models.CharField('Unique Squirrel ID', max_length=100)
    PM = 'PM'
    AM = 'AM'
    SHIFT = (
        (AM,'AM'),
        (PM,'PM'),
    )
    Shift = models.CharField('Shift', max_length=2, choices=SHIFT)
    Date = models.DateField()
    Age = models.CharField('Age', max_length=100)
    Primary_fur_color = models.CharField('Primary Fur Color', max_length=100)
    Location = models.CharField('Location', max_length=100)
    Specific_location = models.CharField('Specific Location', max_length=100)
    Running = models.BooleanField(default=False)
    Chasing = models.BooleanField(default=False)
    Climbing = models.BooleanField(default=False)
    Eating = models.BooleanField(default=False)
    Foraging = models.BooleanField(default=False)
    Other_activities = models.CharField('Other Activities', max_length=100)
    Kuks = models.BooleanField(default=False)
    Quaas = models.BooleanField(default=False)
    Moans = models.BooleanField(default=False)
    Tail_flags = models.BooleanField(default=False)
    Tail_twitches = models.BooleanField(default=False)
    Approaches = models.BooleanField(default=False)
    Indifferent = models.BooleanField(default=False)
    Runs_from = models.BooleanField(default=False)

    def __str__(self):
        return self.Uni
