from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

from .forms import CreateHworkForm
from .models import Hwork, Order

User = get_user_model()


def index(request):
    template = 'hworks/index.html'
    context = {}
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        hworks = Hwork.objects.filter(user=user)
        orders = Order.objects.filter(hwork__in=hworks, is_finished=False)
        context = {
            'orders': orders
        }
    return render(request, template, context)


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user_profile': user}
    template = 'hworks/profile.html'
    return render(request, template, context)


@login_required
def hworks_list(request, username):
    user = get_object_or_404(User, username=username)
    hworks = Hwork.objects.filter(user=user)
    context = {
        'hworks': hworks,
        'seller': user.username
    }
    template = 'hworks/hworks.html'
    return render(request, template, context)


@login_required
def my_hworks(request):
    user = get_object_or_404(User, username=request.user)
    hworks = Hwork.objects.filter(user=user)
    context = {
        'hworks': hworks
    }
    template = 'hworks/my_hworks.html'
    return render(request, template, context)

@method_decorator(login_required, name='dispatch')
class HworkCreate(CreateView):
    form_class = CreateHworkForm
    success_url = reverse_lazy('hworks:my_hworks')
    template_name = 'hworks/hwork_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Новый Hwork создан!')
        return super(HworkCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class HworkUpdate(UpdateView):
    model = Hwork
    fields = ['title', 'description', 'price', 'group']
    success_url = reverse_lazy('hworks:my_hworks')
    template_name = 'hworks/hwork_update.html'
    def get_object(self, queryset=None):
        obj = super(HworkUpdate, self).get_object()
        if not obj.user == self.request.user:
            raise PermissionDenied()
        return obj
    def form_valid(self, form):
        messages.success(self.request, 'Hwork успешно обновлен!')
        return super().form_valid(form)
