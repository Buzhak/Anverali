from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from .forms import CreationForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('hworks:index')
    template_name = 'users/signup.html'


@login_required
def change_status(request, username):
    '''
    Пользователь может изменить свой статус с продовца на покупателя
    '''
    if request.method == 'POST':
        user = get_object_or_404(User, username=username)
        user.is_freelancer = not user.is_freelancer
        user.save()
        return redirect('hworks:index')
    else:
        return HttpResponse('Метод запроса не поддерживается.', status=405)
