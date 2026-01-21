from django.core.management.base import BaseCommand
from django.core.management import call_command
from events.models import Event, Ticket

class Command(BaseCommand):
    help = 'Clears all Events and Tickets, then runs the seed_events command.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Clearing all Ticket records...'))
        Ticket.objects.all().delete()
        
        self.stdout.write(self.style.WARNING('Clearing all Event records...'))
        Event.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Successfully cleared old data.'))
        
        self.stdout.write(self.style.NOTICE('Starting seed_events...'))
        call_command('seed_events')
        
        self.stdout.write(self.style.SUCCESS('Reset and Seed process complete.'))
