import csv
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        l = list()
        l.append(['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location',
            'Running','Climbing','Eating','Foraging','Other_activities','Kuks','Quaas','Moans','Tail flags',
            'Tail twitches','Approaches','Indiffernet','Runs from'])
        for i in Squirrel.objects.all():
            l.append([i.Lat,i.Long,i.Uni,i.Shift,i.Date,i.Age,i.Primary_fur_color,i.Location,i.Specific_location,
                i.Running,i.Chasing,i.Climbing,i.Eating,i.Foraging,i.Other_activities,i.Kuks,i.Quaas,i.Moans,
                i.Tail_flags,i.Tail_twitches,i.Approaches,i.Indifferent,i.Runs_from])
        with open(options['csv_file'],'w',newline='') as fp:
            cw = csv.writer(fp)
            cw.writerows(r for r in l)
