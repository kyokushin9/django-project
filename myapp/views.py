import logging

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index pages')
    return HttpResponse('Hello world')


def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('ooops, something went wrong')
    else:
        logger.debug('About page access')
        return HttpResponse('page about')
