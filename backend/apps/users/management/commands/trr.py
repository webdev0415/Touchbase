##### MOVE ALL TB APPLIANCES (SPF, WTF, ETC.) TO MANAGEMENT COMMANDS LIKE THIS

from django.core.management.base import BaseCommand, CommandError
from apps.users.models import User

class Command(BaseCommand):
    help = 'Goes through every user and resets tri_count, on a cron job to run every 24hr. ! means error'
    
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            try:
                user.settings.tri_count = 0
                user.settings.save()
            except:
                print(f"! for {user.username}")
