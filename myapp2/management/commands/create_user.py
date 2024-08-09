from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **options):
        #self.stdout.write('helo help')
        user = User(name='Ivan', email='ivan@mail.com', password='secret', age=35)
        user.save();
        self.stdout.write(f'{user}')
