from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'Get user'

    def add_arguments(self, parser):
        #parser.add_argument('id', type=int, help='User ID')
        parser.add_argument('age', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        #id = kwargs['id']
        #pk = kwargs['id']
        age = kwargs['age']
        #user = User.objects.get(id=id)
        #user = User.objects.filter(pk=pk).first()
        user = User.objects.filter(age__gt=age)
        self.stdout.write(f'{user}')
