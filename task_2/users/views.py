from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from .forms import CreateUserForm, FullUserForm, ShortUserForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('hworks:index')
    template_name = 'users/signup.html'


@login_required
def change_status(request, username):
    '''
    Пользователь может изменить свой статус с продовца на покупателя
    '''
    if request.method == 'POST':
        previous_url = request.META.get('HTTP_REFERER')
        user = get_object_or_404(User, username=username)
        user.is_freelancer = not user.is_freelancer
        user.save()
        if previous_url:
            return redirect(previous_url)
        return redirect('hworks:index')
    else:
        return HttpResponse('Метод запроса не поддерживается.', status=405)


@login_required
def user_update(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        if user.is_freelancer:
            form = FullUserForm(instance=user)
        else:
            form = ShortUserForm(instance=user)
        template = 'users/edit.html'
        context = {'form': form, 'username': user.get_username()}
        return render(request, template, context)
    elif request.method == 'POST':
        if user.is_freelancer:
            form = FullUserForm(request.POST, instance=user)
        else:
            form = ShortUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('hworks:profile', username=user.username)
    else:
        return HttpResponse('Метод запроса не поддерживается.', status=405)
    
