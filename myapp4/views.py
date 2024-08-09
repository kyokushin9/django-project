import logging
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.core.files.storage import FileSystemStorage
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from .models import User

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')

        else:
            logger.debug(f'Ошибки во время отправки')
    else:
        form = UserForm()

    return render(request, 'myapp4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}')

    else:
        form = ManyFieldsFormWidget()

    return render(request, 'myapp4/many_fields_form.html', {'form': form})



def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message='Пользователь сохранен'

            # try:
            #     send_mail(
            #         "Subject here",
            #         f"Here is the message. Name: {name}, Email: {email}, Age: {age}",
            #         "from@example.com",
            #         ["kyokushin9@yandex.ru"],
            #         fail_silently=False,
            #     )
            # except BadHeaderError:
            #     logger.info('Ошибка в теме письма.')
            # logger.info('success')


        else:
            logger.debug(f'Ошибки во время отправки')
    else:
        form = UserForm()
        message = 'Заполните форму'

    return render(request, 'myapp4/user_form2.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()

    return render(request, 'myapp4/upload_image.html', {'form': form})