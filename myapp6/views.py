from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product


# Create your views here.


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе',
        'total': total
    }

    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количство посчитаное через представление',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее количество посчитанное через шаблон',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)
