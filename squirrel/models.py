from django.db import models
from django.utils.translation import gettext as _



    
class Squirrel(models.Model):
    Lat = models.FloatField('Latitude')
    Long = models.FloatField('Longitude')
    Uni = models.CharField('Unique Squirrel ID',max_length=100)
    PM = 'PM'
    AM = 'AM'
    SHIFT = (
        (AM,'AM'),
        (PM,'PM'),
    )
    Shift = models.CharField('Shift',max_length=2,choices=SHIFT)
    Date = models.DateField()
    Age = models.IntegerField()

    def __str__(self):
        return self.Uni
