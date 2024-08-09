from django.core.management.base import BaseCommand
from myapp2.models import User, Author, Post

class Command(BaseCommand):
    help = 'Generate fake author and post'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'email{i}@ml.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title post {j}',
                    content=f'Content post {j}',
                    author=author
                )
                post.save()


