##### MOVE ALL TB APPLIANCES (SPF, WTF, ETC.) TO MANAGEMENT COMMANDS LIKE THIS

from django.core.management.base import BaseCommand, CommandError
from apps.cliques.models import Clique

class Command(BaseCommand):
    help = 'Goes through every clique and resets tri_count, on a cron job to run every 24hr. ! means error'
    
    def handle(self, *args, **options):
        cliques = Clique.objects.all()
        for clique in cliques:
            try:
                clique.tri_count = 0
                clique.save()
            except:
                print(f"! for {clique.cliquename}")
