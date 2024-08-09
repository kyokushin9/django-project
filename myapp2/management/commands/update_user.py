from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'Get user'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User Name')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}')
