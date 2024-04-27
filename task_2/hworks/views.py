from django.shortcuts import render


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'hworks/index.html'
    # Формируем шаблон
    return render(request, template)
