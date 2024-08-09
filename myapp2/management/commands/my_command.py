from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'print help stroce'

    def handle(self, *args, **options):
        self.stdout.write('helo help')
