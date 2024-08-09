from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'Get all users'

    def handle(self, *args, **options):
        #self.stdout.write('helo help')
        user = User.objects.all()
        self.stdout.write(f'{user}')
