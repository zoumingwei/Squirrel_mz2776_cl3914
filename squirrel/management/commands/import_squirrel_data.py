import csv
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        for item in data:
            p = Squirrel(
                Long=item['X'],
                Lat=item['Y'],
                Shift=item['Shift'],
                Date=item['Date'][-4:]+'-'+item['Date'][:2]+'-'+item['Date'][2:4],
                Age=item['Age'],
                Primary_fur_color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_location=item['Specific Location'],
                Running=item['Running'].lower().capitalize(),
                Chasing=item['Chasing'].lower().capitalize(),
                Climbing=item['Climbing'].lower().capitalize(),
                Eating=item['Eating'].lower().capitalize(),
                Foraging=item['Foraging'].lower().capitalize(),
                Other_activities=item['Other Activities'],
                Kuks=item['Kuks'].lower().capitalize(),
                Quaas=item['Quaas'].lower().capitalize(),
                Moans=item['Moans'].lower().capitalize(),
                Tail_flags=item['Tail flags'].lower().capitalize(),
                Tail_twitches=item['Tail twitches'].lower().capitalize(),
                Approaches=item['Approaches'].lower().capitalize(),
                Indifferent=item['Indifferent'].lower().capitalize(),
                Runs_from=item['Runs from'].lower().capitalize(),
            )
            p.save()
