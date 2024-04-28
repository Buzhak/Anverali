from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'hworks/index.html'
    # Формируем шаблон
    return render(request, template)


@login_required
def profile(request, username):
    template = 'hworks/profile.html'
    return render(request, template)